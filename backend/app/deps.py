from typing import Annotated, AsyncGenerator, TypeAlias
from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.model_db import QuestionDB, AnswerDB
from app.db import async_engine


async def create_session() -> AsyncGenerator[AsyncSession]:
    async with AsyncSession(async_engine) as async_session:
        yield async_session


SessionDep: TypeAlias = Annotated[AsyncSession, Depends(create_session)]


# NOTE: crud operation
async def get_answer_db(session: SessionDep, answer_id: int) -> AnswerDB:
    statement = select(AnswerDB).where(AnswerDB.id == answer_id)
    session_user = await session.scalar(statement)
    if session_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Answer wasn't found"
        )
    return session_user


CurrentAnswerDep: TypeAlias = Annotated[AnswerDB, Depends(get_answer_db)]


# NOTE: crud operation
async def get_question_db(session: SessionDep, question_id: int) -> QuestionDB:
    statement = select(QuestionDB).where(QuestionDB.id == question_id)
    session_question = await session.scalar(statement)
    if session_question is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Question wasn't found"
        )
    return session_question


CurrentQuestionDep: TypeAlias = Annotated[QuestionDB, Depends(get_question_db)]
