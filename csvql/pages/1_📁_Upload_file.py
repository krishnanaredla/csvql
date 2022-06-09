import streamlit as st
import pandas as pd
from pandas.io.json import build_table_schema
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode
from csvql.db import CSVdb
import time
from random import randint

db = CSVdb()
placeholder = st.empty()

if 'upload_key'not in st.session_state:
    st.session_state.upload_key = str(randint(1000, 100000000))

uploaded_file = st.file_uploader(label="Upload CSV file", type=["csv"],key=st.session_state.upload_key)

with st.container():
    if uploaded_file is not None:
        col1, col2 = st.columns(2)
        with col1:
            delimiter = st.text_input(label="Enter Delimiter", value=",")
        with col2:
            header = int(st.text_input(label="Select Header Row", value="0"))
        df = pd.read_csv(uploaded_file, delimiter=delimiter, header=header)
        with st.expander("View Sample Data"):
             st.table(df.head(5))
        schema = pd.DataFrame(build_table_schema(df).get("fields"))
        with st.expander("Modify Schema if needed"):
            gb = GridOptionsBuilder.from_dataframe(schema,enableRowGroup=True, enableValue=True, enablePivot=True)
            gb.configure_default_column(editable=True)
            gb.configure_grid_options(enableRangeSelection=True)#,domLayout='autoHeight')
            response = AgGrid(
                schema,
                gridOptions=gb.build(),
                fit_columns_on_grid_load=True,
                height = 38+(len(df.columns)*26),
                allow_unsafe_jscode=True,
                enable_enterprise_modules=True,
                theme="dark"
            )
        col1, col2 = st.columns(2)
        with col1:
            table_name = st.text_input(label="Save as",value=uploaded_file.name.split('.')[0].replace(' ','_'))
            checkExists = db.checkIfTableExists(table_name)
            if  checkExists:
                st.warning("Table {} already exists".format(table_name))
        with col2:
            if st.button("create table"):
                 createStatus = db.createTable(df,table_name)
                 if createStatus.get('Status') == 1:
                      st.success(createStatus.get('Message'))
                      #time.sleep(10)
                      st.session_state.upload_key = str(randint(1000, 100000000))
                      db.close()
                      time.sleep(3)
                      st.experimental_rerun() 
                 else:
                      st.error(createStatus.get('Message'))


