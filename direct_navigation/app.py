import streamlit as st

st.title("Home")

foo = st.sidebar.slider("Slider")

def page1():
    st.markdown("a page")

def page2():
    st.markdown("another page")

pg = st.navigation([st.Page(page1), st.Page(page2, title="page2")])
pg.run()

st.write(f"**Slider val: `{foo}`**")

