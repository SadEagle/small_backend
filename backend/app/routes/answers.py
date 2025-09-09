from fastapi import APIRouter

from app import crud
from app.deps import CurrentAnswerDep, SessionDep
from app.model_data import Message, Answer

app_answers = APIRouter(prefix="/answers")


@app_answers.get("/{answer_id}")
async def get_answer(current_answer: CurrentAnswerDep) -> Answer:
    return Answer.model_validate(current_answer, from_attributes=True)


@app_answers.delete("/{answer_id}")
async def delete_answer(
    session: SessionDep, current_answer: CurrentAnswerDep
) -> Message:
    await crud.delete_answer_db(session, current_answer)
    return Message(message="Answer was successfully deleted")
