import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.util import was_deleted

from app import crud
from app import deps
from app.model_data import QuestionCreate, AnswerCreate


@pytest.mark.anyio
async def test_create_question(
    session: AsyncSession, question_create: QuestionCreate
) -> None:
    question = await crud.create_question_db(session, question_create)
    assert question.text == question_create.text


@pytest.mark.anyio
async def test_create_answer(
    session: AsyncSession, question_create: QuestionCreate, answer_create: AnswerCreate
) -> None:
    question = await crud.create_question_db(session, question_create)
    answer = await crud.create_answer_db(session, answer_create, question)
    assert answer.text == answer_create.text
    assert answer.question_id == question.id


@pytest.mark.anyio
async def test_delete_question(
    session: AsyncSession, question_create: QuestionCreate
) -> None:
    question = await crud.create_question_db(session, question_create)
    assert question in session
    await crud.delete_question_db(session, question)
    assert was_deleted(question)


@pytest.mark.anyio
async def test_delete_answer(
    session: AsyncSession, question_create: QuestionCreate, answer_create: AnswerCreate
) -> None:
    question = await crud.create_question_db(session, question_create)
    answer = await crud.create_answer_db(session, answer_create, question)
    assert answer in session
    await crud.delete_answer_db(session, answer)
    assert was_deleted(answer)


@pytest.mark.anyio
async def test_get_question_with_answers(
    session: AsyncSession,
    question_create: QuestionCreate,
    answer_create: AnswerCreate,
) -> None:
    question = await crud.create_question_db(session, question_create)
    answer = await crud.create_answer_db(session, answer_create, question)

    question_answers_tuple = await crud.get_question_with_answers_db(
        session, question.id
    )
    assert len(question_answers_tuple) == 1
    assert question_answers_tuple[0] is answer


@pytest.mark.anyio
async def test_is_user_answered_question_db(
    session: AsyncSession,
    question_create: QuestionCreate,
    answer_create: AnswerCreate,
    extra_question_create: QuestionCreate,
) -> None:
    question = await crud.create_question_db(session, question_create)
    extra_question = await crud.create_question_db(session, extra_question_create)
    answer = await crud.create_answer_db(session, answer_create, question)

    is_answered = await crud.is_user_answered_question_db(
        session, answer.user_id, question.id
    )
    assert is_answered

    is_answered = await crud.is_user_answered_question_db(
        session, answer.user_id, extra_question.id
    )
    assert not is_answered


# Test crud from app.deps
@pytest.mark.anyio
async def test_get_question_db(
    session: AsyncSession, question_create: QuestionCreate
) -> None:
    question = await crud.create_question_db(session, question_create)
    question_query = await deps.get_question_db(session, question.id)
    assert question is question_query


# Test crud from app.deps
@pytest.mark.anyio
async def test_get_answer_db(
    session, question_create: QuestionCreate, answer_create: AnswerCreate
) -> None:
    question = await crud.create_question_db(session, question_create)
    answer = await crud.create_answer_db(session, answer_create, question)

    answer_query = await deps.get_answer_db(session, answer.id)
    assert answer is answer_query
