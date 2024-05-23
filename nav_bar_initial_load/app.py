import streamlit as st

def page1():
    st.markdown("a page")
    st.slider("foo")

def page2():
    st.markdown("another page")
    st.page_link("fpp/page3.py")

pages = [
    st.Page(page1, icon=":material/home:", default=True),
    st.Page(page2, icon="🔥", title="Page 2"),
]

# import time
# time.sleep(0.05)

pg = st.navigation({"Section": pages}, position="hidden")
pg.run()

st.write("hello")

st.sidebar.header("MPA test")
