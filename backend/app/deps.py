from typing import Annotated, TypeAlias, Generator
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.model_db import QuestionDB, AnswerDB
from app.db import engine


def create_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SessionDep: TypeAlias = Annotated[Session, Depends(create_session)]


# TODO: Delete n+1 problem by adding extra select with special type
def get_answer_db(session: SessionDep, answer_id: int) -> AnswerDB | None:
    statement = select(AnswerDB).where(AnswerDB.id == answer_id)
    session_user = session.execute(statement).one_or_none()
    if session_user is None:
        return None
    return session_user.scalar()


CurrentAnswerDep: TypeAlias = Annotated[AnswerDB, Depends(get_answer_db)]


# WARN: inproper realization, need aware of n+1
# TODO: add correct loading, need to be aware of n+1 trouble!!!!!
# def get_question_db(session: SessionDep, question_id) -> QuestionDB | None:
#     statement = select(QuestionDB).where(QuestionDB.id == question_id)
#     session_question = session.execute(statement).one_or_none()
#     if session_question is None:
#         return None
#     return session_question.scalar()
#
#
# CurrentQuestionDep: TypeAlias = Annotated[AnswerDB, Depends(get_question_db)]
