import streamlit as st

st.header("Incorrect value of common widgets on page change")

"""
page should run and fail because of material icon
"""

foo = st.sidebar.slider("Slider")

def page1():
    st.markdown("a page")

pg = st.navigation([st.Page(page1, icon=":material/settingszz:"), st.Page(page1, title="page2")])
pg.run()

st.write(f"**Slider val: `{foo}`**")


