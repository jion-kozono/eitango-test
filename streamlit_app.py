import streamlit as st

from streamlit_pages.create_test import createTestPage
from streamlit_pages.test import testPage
from streamlit_utils import utils

utils.init()
page = st.session_state.page
words = st.session_state.words

st.title('英単語テストアプリ')

if page == "create_test":
    createTestPage()
elif page == "test":
    testPage(words)