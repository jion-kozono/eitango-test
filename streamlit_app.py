import streamlit as st
import requests

# page = st.sidebar.selectbox('ページを選択', ["use/rs", "rooms", "bookings"])
st.title('英単語テストアプリ')
st.write('#### テスト情報を入力してください。')

with st.form(key="test-range"):
    book_name: str = st.selectbox("単語帳名", ["1は", "2は", "3は"]) # TODO: 単語帳一覧リストが入る
    first_num: int = st.number_input("最初の単語番号", step=1, min_value=1)
    last_num: int = st.number_input("最後の単語番号", step=1, min_value=2)

    submit_button = st.form_submit_button(label="テストを発行")

if submit_button:
    # 入力値バリデーション
    if first_num >= last_num:
        st.error('最後の単語番号は最初の単語番号より大きくなければなりません。')
    else:
        # ユーザー一覧取得
        url_test_words = f'https://simple-eitango-test.herokuapp.com/words/{book_name}?first={first_num}&last={last_num}'
        res = requests.get(url_test_words)
        if res.status_code == 200:
            words = res.json()
            print(words)
            st.success("テスト作成")
        else:
            st.error("テスト取得に失敗しました。")

