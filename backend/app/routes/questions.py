from fastapi import APIRouter

from app.core.deps import SessionDep
from app.data_models.questions_model import (
    ListQuestions,
    QuestionCreate,
    Question,
    QuestionOutConfirm,
)


app_questions = APIRouter(prefix="/questions")


@app_questions.get("/")
def get_all_questions(session: SessionDep) -> ListQuestions:
    session


@app_questions.get("/{question_id}")
def get_question(question_id: int, session: SessionDep) -> Question:
    pass


@app_questions.post("/{question_id}")
def create_questions(question_id: int, session: SessionDep) -> QuestionOutConfirm:
    pass


@app_questions.delete("/{question_id}")
def delete_id_question(question_id: int, session: SessionDep) -> QuestionOutConfirm:
    pass


@app_questions.post("/{question_id}/answers")
def add_answer_id_question(question_id: int, session: SessionDep) -> Question:
    pass
