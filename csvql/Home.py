import streamlit as st
import pandas as pd
from csvql.db import CSVdb



st.set_page_config(page_icon="🦥", page_title="CSVQL")

with st.sidebar:
    st.image(
        "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/apple/325/sloth_1f9a5.png",
        width=100,
    )
    st.title("CSVQL")
db = CSVdb()
tables = db.getTables()
db.close()
col1, col2, col3 = st.columns([1,1,1])
col2.metric("Total   Tables", "   {} ".format(int(tables.count())))
if int(tables.count())>0:
    col1, col2, col3 = st.columns([1,6,1])
    with col2:
        st.dataframe(tables)
