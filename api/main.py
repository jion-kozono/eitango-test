from fastapi import FastAPI

from routers import word

app = FastAPI()
app.include_router(word.router)