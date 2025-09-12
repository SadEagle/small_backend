from typing import AsyncGenerator
import random
import string


import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import async_engine
from app.main import app
from app.model_db import Base
from app.model_data import AnswerCreate, QuestionCreate


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


# NOTE: Need to make anyio fixture compatile as most wide fixture scope
# Ref: anyio.readthedocs.io/en/stable/testing.html#using-async-fixtures-with-higher-scopes
@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="session", autouse=True)
async def creation_engine_tables() -> AsyncGenerator[None]:
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield None
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="function")
async def session() -> AsyncGenerator[AsyncSession]:
    # WARN: async expects no expiration
    # Ref: https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html#preventing-implicit-io-when-using-asyncsession
    async with AsyncSession(async_engine, expire_on_commit=False) as session:
        yield session


@pytest.fixture(scope="session")
async def client() -> AsyncGenerator[AsyncClient]:
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac


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
