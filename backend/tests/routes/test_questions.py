import pytest
from fastapi import HTTPException, status
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.model_data import AnswerCreate, QuestionCreate
from app.crud import create_answer_db, create_question_db
from app.deps import get_question_db


def test_create_question(
    client: TestClient,
    question_create: QuestionCreate,
) -> None:
    response = client.post(
        "/questions/",
        json=question_create.model_dump(mode="json"),
    )
    assert response.status_code == status.HTTP_201_CREATED


def test_get_question_with_answers(
    client: TestClient,
    session: Session,
    question_create: QuestionCreate,
    answer_create: AnswerCreate,
) -> None:
    question = create_question_db(session, question_create)
    answer = create_answer_db(session, answer_create, question)

    response = client.get(f"/questions/{question.id}")
    assert response.status_code == status.HTTP_200_OK

    content = response.json()
    assert content["question"]["id"] == question.id
    assert len(content["answers"]) == 1
    assert content["answers"][0]["id"] == answer.id


def test_delete_question(
    client: TestClient, session: Session, question_create: QuestionCreate
) -> None:
    question = create_question_db(session, question_create)
    assert get_question_db(session, question.id) is question

    response = client.delete(f"/questions/{question.id}")
    assert response.status_code == status.HTTP_200_OK
    with pytest.raises(HTTPException):
        get_question_db(session, question.id)


def test_create_answer(
    client: TestClient,
    session: Session,
    question_create: QuestionCreate,
    answer_create: AnswerCreate,
) -> None:
    question = create_question_db(session, question_create)

    response = client.post(
        f"/questions/{question.id}/answers", json=answer_create.model_dump(mode="json")
    )
    assert response.status_code == status.HTTP_201_CREATED
