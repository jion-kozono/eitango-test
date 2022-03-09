from typing import Literal
from pydantic import BaseModel, Field

IsCorrect = Literal[0, 1]

class Word(BaseModel):
    word: str
    meaning: str
    book_name: str = Field("Basic Words 早稲田アカデミー")
    word_num: int
    isCorrect: IsCorrect

class PostIsCorrectInput(BaseModel):
    book_name: str
    word_num: int
    isCorrect: IsCorrect