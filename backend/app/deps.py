from typing import Annotated, TypeAlias, Generator
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.model_db import QuestionDB, AnswerDB
from app.db import engine


def create_session() -> Generator[Session]:
    with Session(engine) as session:
        yield session


SessionDep: TypeAlias = Annotated[Session, Depends(create_session)]


# NOTE: crud operation
def get_answer_db(session: SessionDep, answer_id: int) -> AnswerDB:
    statement = select(AnswerDB).where(AnswerDB.id == answer_id)
    session_user = session.scalar(statement)
    if session_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Answer wasn't found"
        )
    return session_user


CurrentAnswerDep: TypeAlias = Annotated[AnswerDB, Depends(get_answer_db)]


# NOTE: crud operation
def get_question_db(session: SessionDep, question_id: int) -> QuestionDB:
    statement = select(QuestionDB).where(QuestionDB.id == question_id)
    session_question = session.scalar(statement)
    if session_question is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Question wasn't found"
        )
    return session_question


CurrentQuestionDep: TypeAlias = Annotated[QuestionDB, Depends(get_question_db)]
