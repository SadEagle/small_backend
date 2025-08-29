from fastapi import APIRouter

from app.deps import CurrentAnswerDep, SessionDep
from app.model_data import Message, Answer

app_answers = APIRouter(prefix="/answers")


@app_answers.get("/{answer_id}")
def get_id_answer(current_answer: CurrentAnswerDep) -> Answer:
    return Answer.model_validate(current_answer, from_attributes=True)


@app_answers.delete("/{answer_id}")
def delete_id_answer(session: SessionDep, current_answer: CurrentAnswerDep) -> Message:
    session.delete(current_answer)
    session.commit()
    return Message(message="Answer was successfully deleted")
