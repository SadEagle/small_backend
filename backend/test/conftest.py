from typing import Generator
import random
import string

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.main import app
from app.deps import engine
from app.model_data import AnswerCreate, QuestionCreate


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


@pytest.fixture(scope="session", autouse=True)
def session() -> Generator[Session]:
    with Session(engine) as session:
        yield session


@pytest.fixture(scope="module")
def client() -> TestClient:
    return TestClient(app)


# NOTE: class objects
@pytest.fixture
def question_create() -> QuestionCreate:
    return QuestionCreate(text=random_lower_string())


@pytest.fixture
def extra_question_create() -> QuestionCreate:
    return QuestionCreate(text=random_lower_string())


@pytest.fixture
def answer_create() -> AnswerCreate:
    return AnswerCreate(
        text=random_lower_string(),
        user_id=random_lower_string(),
    )


@pytest.fixture
def extra_answer_create() -> AnswerCreate:
    return AnswerCreate(
        text=random_lower_string(),
        user_id=random_lower_string(),
    )
