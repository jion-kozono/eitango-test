from typing import List
from fastapi import APIRouter

from schemas import word as word_schema
from cruds import word as word_cruds

router = APIRouter()

@router.get("/books/", response_model=List[str])
async def getAllBooks():
    book_names = word_cruds.getAllBooks()
    return book_names

@router.get("/words/{book_name}", response_model=List[word_schema.Word])
async def getTestWords(book_name: str, first: int, last: int):
    words = word_cruds.getTestWords(book_name, first, last)
    return words

@router.post("/isCorrect/", response_model=None)
async def postIsCorrect(is_correct_list: List[word_schema.PostIsCorrectInput]):
    return word_cruds.postIsCorrect(is_correct_list)

@router.get("/week-words/{book_name}")
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