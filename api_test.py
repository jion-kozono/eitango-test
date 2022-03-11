import json
import requests

from streamlit_utils import constant

def test_post_is_correct():
    data = [
        {
            "id": "ID:1",
            "is_correct": -1,
        },
        {
            "id": "ID:2",
            "is_correct": 1,
        },
    ]
    res = requests.post(
        f'{constant.URL}/isCorrect/',
        data=json.dumps(data)
    )
    print(res.status_code)

if __name__ == '__main__':
    test_post_is_correct()