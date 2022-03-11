import streamlit as st

def init():
    st.set_page_config(
        page_title="英単語テスト",
        page_icon="📕",
        initial_sidebar_state="expanded",
    )
    if 'page' not in st.session_state:
        st.session_state.page = 'create_test'
        st.session_state.words = []

def change_to_test_page():
    st.session_state.page = "test"

def change_to_create_test_page():
    st.session_state.page = "create_test"