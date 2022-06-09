import streamlit as st
from csvql.db import CSVdb
import pandas as pd
import datetime

if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame()

col1, col2 = st.columns([2,6])

db = CSVdb()
tables = db.getTables()
db.close()
tables.rename(columns = {'name':'Tables'}, inplace = True)#
tables.reset_index(drop=True, inplace=True)
with col1:
    #styler = tables.style.hide_index()
    #st.write(styler.to_html(), unsafe_allow_html=True)
    st.dataframe(tables,height=180)
with col2:
    query = st.text_area("Query ...",height=150)

_,run_col,download_col = st.columns([6,1,1])

with run_col:
    if st.button("Execute"):
        db = CSVdb()
        if query == 'Query ...':
            st.warn("Enter Query")
        else:
            st.session_state.data = db.runQuery(query)
with download_col:
    st.download_button("Download",data=st.session_state.data.to_csv(index=False).encode('utf-8'),
    file_name = "file_{}.csv".format(datetime.datetime.now().strftime('%Y%m%H%M%S')),
    mime='text/csv'
    )

st.dataframe(st.session_state.data)