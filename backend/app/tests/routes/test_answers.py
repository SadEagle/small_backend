import pytest
from fastapi import status, HTTPException
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.crud import create_answer_db, create_question_db
from app.model_data import AnswerCreate, QuestionCreate
from app.deps import get_answer_db


def test_get_answer(
    client: TestClient,
    session: Session,
    question_create: QuestionCreate,
    answer_create: AnswerCreate,
) -> None:
    question = create_question_db(session, question_create)
    answer = create_answer_db(session, answer_create, question)

    response = client.get(f"/answers/{answer.id}")

    assert response.status_code == status.HTTP_200_OK
    content = response.json()
    assert content["id"] == answer.id


def test_delete_answer(
    client: TestClient,
    session: Session,
    question_create: QuestionCreate,
    answer_create: AnswerCreate,
) -> None:
    question = create_question_db(session, question_create)
    answer = create_answer_db(session, answer_create, question)

    assert get_answer_db(session, answer.id) is not None
    client.delete(f"/answers/{answer.id}")
    with pytest.raises(HTTPException):
        get_answer_db(session, answer.id)


def test_delete_question_cascade(
    client: TestClient,
    session: Session,
    question_create: QuestionCreate,
    answer_create: AnswerCreate,
) -> None:
    question = create_question_db(session, question_create)
    answer = create_answer_db(session, answer_create, question)
    assert get_answer_db(session, answer.id) is answer

    response = client.delete(f"/questions/{question.id}")
    assert response.status_code == status.HTTP_200_OK
    with pytest.raises(HTTPException):
        get_answer_db(session, answer.id)
