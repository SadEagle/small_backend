from fastapi import FastAPI

from app.routes.question import app_questions


app = FastAPI()
app.include_router(app_questions)
