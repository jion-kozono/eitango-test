import streamlit as st
import requests
import pandas as pd

from streamlit_utils import utils

utils.init()
page = st.session_state.page
words = st.session_state.words

st.title('英単語テストアプリ')

if page == "create_test":
    st.write('#### テスト情報を入力してください。')

    with st.form(key="test-info"):
        # url_books = 'https://simple-eitango-test.herokuapp.com/books/'
        url_books = 'http://0.0.0.0:8000/books/'
        res = requests.get(url_books)
        book_names = res.json()
        book_name: str = st.selectbox("単語帳名", book_names)
        first_num: int = st.number_input("最初の単語番号", step=1, min_value=1)
        last_num: int = st.number_input("最後の単語番号", step=1, min_value=2)

        submit_button = st.form_submit_button(label="テストを作成")

    if submit_button:
        # 入力値バリデーション
        if first_num >= last_num:
            st.error('最後の単語番号は最初の単語番号より大きくなければなりません。')
        elif book_name not in book_names:
            st.error(f'{book_name}という単語帳はありません。')
        else:
            # ユーザー一覧取得
            # url_test_words = f'https://simple-eitango-test.herokuapp.com/words/{book_name}?first={first_num}&last={last_num}'
            url_test_words = f'http://0.0.0.0:8000/words/{book_name}?first={first_num}&last={last_num}'
            res = requests.get(url_test_words)
            if res.status_code == 200:
                words = res.json()
                st.session_state.words = words
                st.success("テスト作成成功！")
                st.button("作成したテストを開く", on_click=utils.change_to_test_page)
            else:
                st.error("テスト取得に失敗しました。")

elif page == "test":
    st.write('#### テストに解答してください')
    with st.form(key="test"):
        # 正誤判定したリストと間違えた単語リストを作成
        isCorrect_list_of_dict = []
        wrong_words = []
        for word_info in words:
            word = word_info["word"]
            word_num = word_info["word_num"]
            meaning = word_info["meaning"]
            index = words.index(word_info)
            input_word: str = st.text_input(f'{index + 1}. {meaning} (No. {word_num})', key=index)
            isCorrect = 0
            if input_word == word:
                isCorrect = 1
            else:
                isCorrect = 0
                wrong_words.append({
                    "": index + 1,
                    "あなたの答え": input_word,
                    "英単語": word,
                    "意味": meaning,
                    "No.": word_num,
                })
            isCorrect_dict = {
                "word_num": word_num,
                "word": word,
                "isCorrect": isCorrect,
            }
            isCorrect_list_of_dict.append(isCorrect_dict)

        submit_button = st.form_submit_button(label="解答を送信")

    if submit_button:
        # スコア表示
        score: int = len(list(filter(lambda dict: dict["isCorrect"] == 1, isCorrect_list_of_dict)))
        st.success(f'{score}/{len(words)}点')

        # 間違えた問題を表示
        st.write('#### 間違えた単語')
        df_wrong_words = pd.DataFrame(wrong_words)
        # 余計な列を消す
        hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)

        st.table(df_wrong_words)
        st.write(isCorrect_list_of_dict)

