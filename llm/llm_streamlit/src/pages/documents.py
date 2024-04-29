import streamlit as st
import os
import glob
import pathlib
import pandas as pd
from lib.llamaindex_extension import CustomPDFReader
from pathlib import Path
from langchain.chat_models import ChatOpenAI
from llama_index.core.service_context import ServiceContext
from llama_index.core.storage.storage_context import StorageContext
from llama_index.core.indices.loading import load_index_from_storage
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, ColumnsAutoSizeMode
import base64

st.set_page_config(layout="wide")

DATA_SAVE_PATH = "data/pdf"

SEARCH_TEMPLATE = """
{user_msg}について関連する文書を以下のjson形式で教えてください。
'''
{
    'documents': [
        'document': 'contract1.pdf',
        'page': 2,
        'overview': 'contract1の税金に関する契約を説明した部分です'
    ]
}
'''
"""

storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)

with st.sidebar:
    with st.container():
        st.subheader("Upload")
        uploaded_files = st.file_uploader(
            label="Please upload the file.",
            type="pdf",
            accept_multiple_files=True,
            label_visibility="collapsed"
        )

        if uploaded_files:
            my_bar = st.progress(0)
            for i, uploaded_file in enumerate(uploaded_files):
                with open(os.path.join(DATA_SAVE_PATH, uploaded_file.name), "wb") as f:
                    my_bar.progress(i, f"uploading... {i+1}/{len(uploaded_files)}")
                    f.write(uploaded_file.getbuffer())

                    documents = CustomPDFReader().load_data(file=Path(f.name))

                    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
                    service_context = ServiceContext.from_defaults(llm=llm)

                    for document in documents:
                        index.insert(document)
                        
            index.storage_context.persist()
    
    st.divider()
    with st.container():
        st.subheader("GPT Setting")
        gpt_model = st.selectbox(label="Model", options=["gpt-3.5-turbo", "gpt-4-32k"])
        similality_top_k = st.number_input(label="Similality Document Number", min_value=1)

col1, col2 = st.columns(2, gap="large")
with col1:
    st.subheader("リスト")
    files_path = [pathlib.Path(file) for file in glob.glob(os.path.join(DATA_SAVE_PATH, "*.pdf"))]
    df = pd.DataFrame({"pdf":[file_path.name for file_path in files_path]})
    
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_selection(selection_mode="single", use_checkbox=True)
    gb.configure_pagination()
    gb.configure_side_bar()
    
    gridOptions = gb.build()

    data = AgGrid(df, gridOptions=gridOptions,height=400, columns_auto_size_mode=1)
    
    if question:= st.text_input(label="検索"):
        with st.spinner(text="考え中..."):
            query_engine = index.as_query_engine(similarity_top_k=5)
            answer = query_engine.query(question)#SEARCH_TEMPLATE.format(user_msg=question))
            st.write(answer.response)
            for node in answer.source_nodes:
                st.write(f"{node.metadata['file_name']} ({node.metadata['page_label']}ページ)")

            # TODO metadataでフィルターをかけてから処理

with col2:
    rows = data["selected_rows"]
    if len(rows)>0:
        with open(f"data/pdf/{rows[0]['pdf']}", "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="1000" height="1000" type="application/pdf">'
            st.markdown(pdf_display, unsafe_allow_html=True)