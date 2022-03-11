import streamlit as st
import requests

from streamlit_utils import utils, constant


def createTestPage():
    st.write('#### テスト情報を入力してください。')

    with st.form(key="test-info"):
        url_books = f'{constant.URL}/books/'
        res = requests.get(url_books)
        book_names = res.json()
        book_name: str = st.selectbox("単語帳名", book_names)
        first_num: int = st.number_input("最初の単語番号", step=1, min_value=1)
        last_num: int = st.number_input("最後の単語番号", step=1, min_value=2)
        isOnlyWeek: bool = st.checkbox("苦手だけ（間違ったままの単語が出題されます）")

        submit_button = st.form_submit_button(label="テストを作成")

    if submit_button:
        # 入力値バリデーション
        if first_num >= last_num:
            st.error('最後の単語番号は最初の単語番号より大きくなければなりません。')
        elif book_name not in book_names:
            st.error(f'{book_name}という単語帳はありません。')
        else:
            # テスト単語一覧取得
            url_test_words = f'{constant.URL}/words/{book_name}?first={first_num}&last={last_num}'
            res = requests.get(url_test_words)
            if res.status_code == 200:
                words = res.json()
                st.session_state.words = words
                st.success("テスト作成成功！")
                st.button("作成したテストを開く", on_click=utils.change_to_test_page)
            else:
                st.error("テスト取得に失敗しました。")
