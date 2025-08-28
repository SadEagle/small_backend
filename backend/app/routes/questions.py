from fastapi import APIRouter
from sqlalchemy import select

from app.deps import SessionDep
from app.model_data import AnswerCreate, Question
from app.model_db import QuestionDB


app_questions = APIRouter(prefix="/questions")


# TODO: make bulk-fromat operation .executemany
@app_questions.get("/")
def get_all_questions(session: SessionDep) -> list[Question]:
    pass


@app_questions.get("/{question_id}")
def get_question(current_question: CurrentQuestionDep) -> Question:
    pass


@app_questions.post("/{question_id}")
def create_questions(question_id: int, session: SessionDep) -> Message:
    pass


# Add cascade
@app_questions.delete("/{question_id}")
def delete_id_question(question_id: int, session: SessionDep) -> Message:
    pass


@app_questions.post("/{question_id}/answers")
def add_answer_id_question(
    question_id: int, session: SessionDep, answer_create: AnswerCreate
) -> Question:
    pass
