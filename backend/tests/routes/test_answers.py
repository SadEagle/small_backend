import pytest
from fastapi import status, HTTPException
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import create_answer_db, create_question_db
from app.model_data import AnswerCreate, QuestionCreate
from app.deps import get_answer_db


@pytest.mark.anyio
async def test_get_answer(
    client: AsyncClient,
    session: AsyncSession,
    question_create: QuestionCreate,
    answer_create: AnswerCreate,
) -> None:
    question = await create_question_db(session, question_create)
    answer = await create_answer_db(session, answer_create, question)

    response = await client.get(f"/answers/{answer.id}")

    assert response.status_code == status.HTTP_200_OK
    content = response.json()
    assert content["id"] == answer.id


@pytest.mark.anyio
async def test_delete_answer(
    client: AsyncClient,
    session: AsyncSession,
    question_create: QuestionCreate,
    answer_create: AnswerCreate,
) -> None:
    question = await create_question_db(session, question_create)
    answer = await create_answer_db(session, answer_create, question)

    assert await get_answer_db(session, answer.id) is not None
    await client.delete(f"/answers/{answer.id}")
    with pytest.raises(HTTPException):
        await get_answer_db(session, answer.id)


@pytest.mark.anyio
async def test_delete_question_cascade(
    client: AsyncClient,
    session: AsyncSession,
    question_create: QuestionCreate,
    answer_create: AnswerCreate,
) -> None:
    question = await create_question_db(session, question_create)
    answer = await create_answer_db(session, answer_create, question)
    assert await get_answer_db(session, answer.id) is answer

    response = await client.delete(f"/questions/{question.id}")
    assert response.status_code == status.HTTP_200_OK
    with pytest.raises(HTTPException):
        await get_answer_db(session, answer.id)
