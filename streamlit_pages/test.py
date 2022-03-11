import streamlit as st
import pandas as pd
import requests

from streamlit_utils import utils

def testPage(words):
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