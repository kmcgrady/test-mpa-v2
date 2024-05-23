import streamlit as st

st.title("Home")

foo = st.sidebar.slider("Slider")

def page1():
    st.markdown("a page")

def page2():
    st.markdown("another page")

"""
**REPRO STEPS:**
1. Move the slider
2. Navigate to page2
3. Observe: The slider visually resets to 0
4. Move the slider again
5. Navigate to page1
6. Observe: Now the slider sticks on FE (but BE value resets)
"""

pg = st.navigation([st.Page(page1), st.Page(page2, title="page2")])
pg.run()

st.write(f"**Slider val: `{foo}`**")

