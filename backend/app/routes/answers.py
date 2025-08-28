from fastapi import APIRouter

from app.core.deps import SessionDep
from app.data_models.answers_model import AnswerCreate, Answer, AnswerOutConfirm

app_answers = APIRouter(prefix="/answers")


@app_answers.get("/{answer_id}")
def get_id_answer(answer_id: int, session: SessionDep) -> Answer:
    pass


@app_answers.delete("/{answer_id}")
def delete_id_answer(answer_id: int, session: SessionDep) -> AnswerOutConfirm:
    pass
