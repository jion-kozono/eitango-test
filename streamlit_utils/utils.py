import streamlit as st

def init():
    if 'page' not in st.session_state:
        st.session_state.page = 'create_test'
        st.session_state.words = []

def change_to_test_page():
    st.session_state.page = "test"

def change_to_create_test_page():
    st.session_state.page = "create_test"