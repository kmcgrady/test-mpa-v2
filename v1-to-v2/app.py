import streamlit as st

st.title("App")

pg = st.navigation([
  st.Page("pages/page1.py"),
  st.Page("pages/page2.py")
])
pg.run()