import streamlit as st
import requests

from streamlit_utils.requests import getAllBookNames, getAllWeekWords, getTestWords
from streamlit_utils.utils import change_page

def createTestPage():
    st.button("全ての苦手単語をテストする", on_click=lambda: [getAllWeekWords, change_page("test")])
    st.write('#### テスト情報を入力してください。')

    with st.form(key="test-info"):
        book_names = getAllBookNames()
        book_name: str = st.selectbox("単語帳名", book_names)
        first_num: int = st.number_input("最初の単語番号", step=1, min_value=1)
        last_num: int = st.number_input("最後の単語番号", step=1, min_value=2)
        is_only_week: bool = st.checkbox("苦手だけ（間違ったままの単語が出題されます）")

        submit_button = st.form_submit_button(label="テストを作成")

    if submit_button:
        # 入力値バリデーション
        if first_num >= last_num:
            st.error('最後の単語番号は最初の単語番号より大きくなければなりません。')
        elif book_name not in book_names:
            st.error(f'{book_name}という単語帳はありません。')
        else:
            # テスト単語一覧取得
            res = getTestWords(book_name, first_num, last_num, is_only_week)
            if res.status_code == 200:
                words = res.json()
                if len(words) != 0:
                    st.session_state.words = words
                    st.success("テスト作成成功！")
                    st.button("作成したテストを開く", on_click=change_page("test"))
                else:
                    st.error("苦手単語はありません。")
            else:
                st.error("テスト作成に失敗しました。")
