from fastapi import FastAPI

from api.routers import word

app = FastAPI()
app.include_router(word.router)