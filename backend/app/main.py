from fastapi import FastAPI

from app.routes.questions import app_questions
from app.routes.answers import app_answers


app = FastAPI()
app.include_router(app_questions)
app.include_router(app_answers)
