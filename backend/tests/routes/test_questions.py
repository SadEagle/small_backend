import pytest
from fastapi import status, HTTPException
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.model_data import AnswerCreate, QuestionCreate
from app.crud import create_answer_db, create_question_db
from app.deps import get_question_db


@pytest.mark.anyio
async def test_create_question(
    client: AsyncClient,
    question_create: QuestionCreate,
) -> None:
    response = await client.post(
        "/questions/",
        json=question_create.model_dump(mode="json"),
    )
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.anyio
async def test_get_question_with_answers(
    client: AsyncClient,
    session: AsyncSession,
    question_create: QuestionCreate,
    answer_create: AnswerCreate,
) -> None:
    question = await create_question_db(session, question_create)
    answer = await create_answer_db(session, answer_create, question)

    response = await client.get(f"/questions/{question.id}")
    assert response.status_code == status.HTTP_200_OK

    content = response.json()
    assert content["question"]["id"] == question.id
    assert len(content["answers"]) == 1
    assert content["answers"][0]["id"] == answer.id


@pytest.mark.anyio
async def test_delete_question(
    client: AsyncClient, session: AsyncSession, question_create: QuestionCreate
) -> None:
    question = await create_question_db(session, question_create)
    assert await get_question_db(session, question.id) is question

    response = await client.delete(f"/questions/{question.id}")
    assert response.status_code == status.HTTP_200_OK
    with pytest.raises(HTTPException):
        await get_question_db(session, question.id)


@pytest.mark.anyio
async def test_create_answer(
    client: AsyncClient,
    session: AsyncSession,
    question_create: QuestionCreate,
    answer_create: AnswerCreate,
) -> None:
    question = await create_question_db(session, question_create)

    response = await client.post(
        f"/questions/{question.id}/answers", json=answer_create.model_dump(mode="json")
    )
    assert response.status_code == status.HTTP_201_CREATED
