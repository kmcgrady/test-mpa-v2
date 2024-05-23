import streamlit as st

st.header("Incorrect value of common widgets on page change")

"""
**REPRO STEPS:**
1. Move the slider
2. Navigate to page2
3. Observe: Slider value shows 0
4. Manually rerun page, observe slider value is correct
"""

foo = st.sidebar.slider("Slider")

def page1():
    st.markdown("a page")

pg = st.navigation([st.Page(page1), st.Page(page1, title="page2")])
pg.run()

st.write(f"**Slider val: `{foo}`**")

