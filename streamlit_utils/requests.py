import json
import requests
import streamlit as st

from streamlit_utils.constant import URL

def getAllWeekWords():
    url_week_words = f'{URL}/weekWords/'
    res = requests.get(url_week_words)
    return res.json()

def getAllBookNames():
    url_books = f'{URL}/books/'
    res = requests.get(url_books)
    return res.json()

def getTestWords(book_name, first_num, last_num, is_only_week):
    url_test_words = f'{URL}/words/{book_name}?first={first_num}&last={last_num}&is_only_week={is_only_week}'
    res = requests.get(url_test_words)
    return res # json化しない

def postIsCorrect(is_correct_list_of_dict):
    requests.post(
        f'{URL}/isCorrect/',
        data=json.dumps(is_correct_list_of_dict)
    )
