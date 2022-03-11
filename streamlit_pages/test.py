import streamlit as st
import pandas as pd

from streamlit_utils.requests import postIsCorrect
from streamlit_utils.utils import backToCreateTestPage

def testPage(words):
    st.write('#### テストに解答してください')
    with st.form(key="test"):
        # 正誤判定したリストと間違えた単語リストを作成
        is_correct_list_of_dict = []
        wrong_words = []
        score = 0

        for word_info in words:
            word = word_info["word"]
            word_num = word_info["word_num"]
            meaning = word_info["meaning"]
            index = words.index(word_info)
            input_word: str = st.text_input(f'{index + 1}. {meaning} (No. {word_num})', key=index)
            is_correct = -1
            if input_word == word:
                is_correct = 1
                score += 1
            else:
                is_correct = -1
                wrong_words.append({
                    "": index + 1,
                    "あなたの答え": input_word,
                    "英単語": word,
                    "意味": meaning,
                    "No.": word_num,
                })
            is_correct_dict = {
                "id": word_info["id"],
                "is_correct": int(is_correct),
            }
            is_correct_list_of_dict.append(is_correct_dict)

        submit_button = st.form_submit_button(label="解答を送信")

    if submit_button:
        # スコア表示
        score_text = f'{score}/{len(words)}点'
        if score == len(words):
            st.success(score_text)
            st.success("全問正解！")
        else:
            st.error(score_text)
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
            st.write('**間違えた問題は繰り返し復讐しましょう。**')

        postIsCorrect(is_correct_list_of_dict)

    backToCreateTestPage()