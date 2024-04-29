import streamlit as st
import os
import pandas as pd
from lib.llamaindex_extension import CustomPDFReader
from pathlib import Path
from langchain.chat_models import ChatOpenAI
from llama_index.core.service_context import ServiceContext
from llama_index.core.storage.storage_context import StorageContext
from llama_index.core.indices.loading import load_index_from_storage

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

USER_NAME = "Me"
ASSISTANT_NAME = "GPT"

def add_new_thread():
    first_chat = {"name":ASSISTANT_NAME, "msg":"何かご質問はありますか？"}
    st.session_state.chat_log[f"{os.getlogin()}"][f"New{len(st.session_state.chat_log[f'{os.getlogin()}'])+1}"] = [first_chat]

def delete_selected_thread():
    del st.session_state.chat_log[f"{os.getlogin()}"][selected_thread]

def horizontal_panel(*args):
    if len(args)==0: return
    cols = st.columns(len(args))
    for i,col in enumerate(cols):
        with col: args[i]


if os.path.exists("./storage"):
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    index = load_index_from_storage(storage_context)

# チャットログを保存したセッション情報を初期化
if "chat_log" not in st.session_state:
    first_chat = {"name":ASSISTANT_NAME, "msg":"何かご質問はありますか？"}
    st.session_state.chat_log = {f"{os.getlogin()}":{"New":[first_chat]}}

with st.sidebar:
    selected_thread = st.selectbox(label="Threads", options=[thread_name for thread_name in st.session_state.chat_log[f"{os.getlogin()}"]])
    col1, col2 = st.columns(2)
    with col1: st.button(label="追加", on_click=add_new_thread)
    if len(st.session_state.chat_log[f"{os.getlogin()}"])>1: 
        with col2: 
            st.button(label="削除", on_click=delete_selected_thread)
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

    st.subheader("GPT Setting")
    gpt_model = st.selectbox(label="Model", options=["gpt-3.5-turbo", "gpt-4-32k"])
    similality_top_k = st.number_input(label="Similality Document Number", min_value=1)



# 以前のチャットログを表示
for chat in st.session_state.chat_log[f"{os.getlogin()}"][selected_thread]:
    #avator = avator_img_dict.get(chat["name"], None)
    with st.chat_message(chat["name"]):#, avatar=avator):
        st.write(chat["msg"])

if user_msg:= st.chat_input("ここにメッセージを入力"):
    with st.chat_message(USER_NAME):
        st.write(user_msg)
    # 最新のメッセージを表示
    # query_engine = index.as_chat_engine(similarity_top_k=5)
    # assistant_msg = query_engine.query(user_msg)#query_engine.query(CHAT_TEMPLATE.format(user_msg=user_msg))
    assistant_msg = "AAA"
    with st.chat_message(ASSISTANT_NAME):
        st.write(assistant_msg)#assistant_msg.response)
        # for node in assistant_msg:#.source_nodes:
        #     st.write(f"{node.metadata['file_name']} ({node.metadata['page_label']}ページ)")
        #     st.link_button(node.metadata['file_name'])

    # セッションにチャットログを追加
    st.session_state.chat_log[f"{os.getlogin()}"][selected_thread].append({"name": USER_NAME, "msg": user_msg})
    st.session_state.chat_log[f"{os.getlogin()}"][selected_thread].append({"name": ASSISTANT_NAME, "msg": assistant_msg})