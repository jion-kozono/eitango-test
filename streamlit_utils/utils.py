import streamlit as st

# import streamlit.components.v1 as components

def init():
    st.set_page_config(
        page_title="英単語テスト",
        page_icon="📕",
        initial_sidebar_state="expanded",
    )
    # # TODO: ホーム画面に追加できるようにする
    # components.html(
    #     """
    #     <meta name="mobile-web-app-capable" content="yes">
    #     """
    # )
    if 'page' not in st.session_state:
        st.session_state.page = 'create_test'
        st.session_state.words = []

def change_page(page):
    if page == "test" and len(st.session_state.words) == 0:
        st.error("苦手単語はありません。")
    else:
        st.session_state.page = page

def changeWords(words):
    st.session_state.words = words

def backToCreateTestPage():
    st.button("テスト作成画面に戻る", on_click=lambda: [changeWords(None), change_page("create_test")])