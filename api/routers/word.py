from typing import List
from fastapi import APIRouter

from schemas import word as word_schema
from spreadsheet import sheet

router = APIRouter()

@router.get("/words/{book_name}/", response_model=List[word_schema.Word])
async def getTestWords(first: int, last: int):
    book_name = "Basic Words 早稲田アカデミー"
    list_of_dicts = sheet.get_all_records()
    filtered_list = list(filter(lambda i: i["book_name"] == book_name and first <= i["word_num"] <= last , list_of_dicts))
    return filtered_list

@router.get("/week-words/{book_name}/")
async def getTesWeektWords(first: int, last: int):
    return {
        "message": "getTesWeektWords",
        "first": first,
        "last": last
    }

@router.get("/week-words/}")
async def getWeekWords(first: int, last: int):
    return {
        "message": "getWeekWords",
        "first": first,
        "last": last
    }


@router.post("/isCorrect/")
async def postIsCorrect(req: List[word_schema.PostIsCorrectInput]):
    return req