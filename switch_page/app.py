import streamlit as st

foo = st.sidebar.header("MPA test")

def page1():
    st.markdown("a page")

def page2():
    st.markdown("another page")

pages = [st.Page(page1), st.Page(page2, title="page2")]
st.navigation(pages, position="hidden").run()

st.page_link(pages[0])
if st.button("Page 2"):
    st.switch_page(pages[1])
