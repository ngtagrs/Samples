import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, ColumnsAutoSizeMode


data = {
    'row_labels': [101, 102, 103, 104, 105, 106, 107],
    'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
    'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai',
             'Manchester', 'Cairo', 'Osaka'],
    'age': [41, 28, 33, 34, 38, 31, 37],
    'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
}
df = pd.DataFrame(data)

# select the columns you want the users to see
gb = GridOptionsBuilder.from_dataframe(df)
# configure selection
gb.configure_selection(selection_mode="single")
gb.configure_side_bar()
gb.configure_pagination()
gb.configure_column("Download")
gb.configure_column("Delete")
gb.configure_columns()
gridOptions = gb.build()

data = AgGrid(df,
              gridOptions=gridOptions,
              enable_enterprise_modules=True,
              allow_unsafe_jscode=True,
              update_mode=GridUpdateMode.SELECTION_CHANGED,
              columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS)

selected_rows = data["selected_rows"]

if len(selected_rows) != 0:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("##### Name")
        st.markdown(f":orange[{selected_rows[0]['name']}]")
    with col2:
        st.markdown("##### City")
        st.markdown(f":orange[{selected_rows[0]['city']}]")
    with col3:
        st.markdown("##### Age")
        st.markdown(f":orange[{selected_rows[0]['age']}]")
    with col4:
        st.markdown("##### Py Score")
        st.markdown(f":orange[{selected_rows[0]['py-score']}]")

import base64
with open("data/pdf/Robust Deep Hedging.pdf", "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

def create_threads_container(name:str):
    with st.container():
        col1,col2 = st.columns([1,2])
        with col1: st.write(name)
        with col2: st.button(label="x")

with st.sidebar:
    st.button(label="222")
    create_threads_container("test")
