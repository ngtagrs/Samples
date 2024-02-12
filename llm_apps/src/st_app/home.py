import streamlit as st
import streamlit.components.v1 as components
from awesome_table import AwesomeTable
from awesome_table.column import (Column, ColumnDType)
import os
import glob
import pathlib
import pandas as pd
from lib.llamaindex_extension import CustomPDFReader
from pathlib import Path
from langchain.chat_models import ChatOpenAI
from llama_index import ServiceContext, VectorStoreIndex
from llama_index import StorageContext, load_index_from_storage
from streamlit_sortables import sort_items

st.set_page_config(layout="wide")

DATA_SAVE_PATH = "data/pdf"

CHAT_TEMPLATE = """
{user_msg}

参考にした文書がある場合は以下のjson形式で教えてください。
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

                    # index = VectorStoreIndex.from_documents(
                    #     documents=documents, service_context=service_context
                    # )
                    #st.session_state["index"] = index
                        
            index.storage_context.persist()
    
    st.divider()
    with st.container():
        st.subheader("GPT Setting")
        gpt_model = st.selectbox(label="Model", options=["gpt-3.5-turbo", "gpt-4-32k"])
        similality_top_k = st.number_input(label="Similality Document Number", min_value=1)

col1, col2 = st.columns(2, gap="large")
with col1:
    st.subheader("契約書リスト")
    files_path = [pathlib.Path(file) for file in glob.glob(os.path.join(DATA_SAVE_PATH, "*.pdf"))]
    df = pd.DataFrame({"pdf":[file_path.name for file_path in files_path], "path": [file_path.name for file_path in files_path]})
    # st.dataframe(df,
    #              column_config={
    #                  "pdf": st.column_config.LinkColumn(
    #                      "PDF"
    #                  ),
    #                  "path": st.column_config.Column(
    #                      "Download",
    #                  )
    #              })
    
    AwesomeTable(df, columns=[
        Column(name="pdf", label="PDF"),
        Column(name='path', label="Download", dtype=ColumnDType.DOWNLOAD),
        Column(name='path', label="Delete", dtype=ColumnDType.ICONBUTTON,  icon="fa-solid fa-share-nodes"),
        ], show_search=True, show_order=True)

with col2:
    # index_dic = index.storage_context.to_dict()
    # targets = set(["ALL"])
    # for node in index_dic["doc_store"]["docstore/ref_doc_info"].values():
    #     targets.add(node["metadata"]["file_name"])
    # st.selectbox(label="Select target documents", options=targets)
    st.subheader("GPT")
    if index is not None:
        gpt_col1, gpt_col2 = st.columns(2)
        with gpt_col1: method = st.selectbox(label="method", options=["Chat", "検索"])
        if method == "Chat":
            with gpt_col2: document = st.selectbox(label="document", options=["ALL"])

            with st.container(border=True, height=1000):
                chat_col1, chat_col2 = st.columns(2)
                USER_NAME = "Me"
                ASSISTANT_NAME = "GPT"
                # チャットログを保存したセッション情報を初期化
                if "chat_log" not in st.session_state:
                    first_chat = {"name":ASSISTANT_NAME, "msg":"何かご質問はありますか？"}
                    st.session_state.chat_log = [first_chat]
                    with chat_col1:
                        with st.chat_message(first_chat["name"]):#, avatar=avator):
                                st.write(first_chat["msg"])

                # # ユーザーのアバターを設定
                # avator_img_dict = {
                #     MORIAGE_YAKU_NAME: "🎉",
                # }

                user_msg = st.chat_input("ここにメッセージを入力")
                if user_msg:
                    # 以前のチャットログを表示
                    for chat in st.session_state.chat_log:
                        col = chat_col1 if chat["name"]==ASSISTANT_NAME else chat_col2
                        with col:
                            #avator = avator_img_dict.get(chat["name"], None)
                            with st.chat_message(chat["name"]):#, avatar=avator):
                                st.write(chat["msg"])
                    
                    with chat_col2:
                        with st.chat_message(USER_NAME):
                            st.write(user_msg)
                    # 最新のメッセージを表示
                    query_engine = index.as_query_engine(similality_top_k=5)
                    assistant_msg = query_engine.query(user_msg)#query_engine.query(CHAT_TEMPLATE.format(user_msg=user_msg))
                    with chat_col1:
                        with st.chat_message(ASSISTANT_NAME):
                            st.write(assistant_msg.response)
                            for node in assistant_msg.source_nodes:
                                st.write(f"{node.metadata['file_name']} ({node.metadata['page_label']}ページ)")

                    # セッションにチャットログを追加
                    st.session_state.chat_log.append({"name": USER_NAME, "msg": user_msg})
                    st.session_state.chat_log.append({"name": ASSISTANT_NAME, "msg": user_msg})

        elif method=="検索":
            question = st.text_input(label="質問")
            if question:
                with st.spinner(text="考え中..."):
                    query_engine = index.as_query_engine(similality_top_k=5)
                    answer = query_engine.query(SEARCH_TEMPLATE.format(user_msg=question))
                    st.write(answer.response)
                    for node in answer.source_nodes:
                        st.write(f"{node.metadata['file_name']} ({node.metadata['page_label']}ページ)")

                    # TODO metadataでフィルターをかけてから処理