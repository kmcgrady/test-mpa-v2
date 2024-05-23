import streamlit as st

def page1():
  st.header("Main Page")

def page2():
  st.header("Main Page")

st.set_page_config("Don't Override me!", ":material/face:")

pg = st.navigation([st.Page(page1, title="Page 1", icon=":material/settings:"),st.Page(page1, title="Page 2", icon=":material/build:")])
pg.run()
