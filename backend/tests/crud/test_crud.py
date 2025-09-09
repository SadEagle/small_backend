from sqlalchemy.orm import Session
from sqlalchemy.orm.util import was_deleted
import pytest

from app import crud
from app.model_data import QuestionCreate, AnswerCreate
from app.model_db import AnswerDB, QuestionDB
from app.deps import get_answer_db, get_question_db


def test_create_question(session: Session, question_create: QuestionCreate) -> None:
    question = crud.create_question_db(session, question_create)
    assert question.text == question_create.text


def test_create_answer(
    session: Session, question_create: QuestionCreate, answer_create: AnswerCreate
) -> None:
    question = crud.create_question_db(session, question_create)
    answer = crud.create_answer_db(session, answer_create, question)
    assert answer.text == answer_create.text
    assert answer.question_id == question.id


def test_delete_question(session: Session, question_create: QuestionCreate) -> None:
    question = crud.create_question_db(session, question_create)
    # TODO: check if better option and replace same way all other options
    # assert question in session
    assert session.get(QuestionDB, question.id) is not None

    crud.delete_question_db(session, question)
    assert was_deleted(question)


def test_delete_answer(
    session: Session, question_create: QuestionCreate, answer_create: AnswerCreate
) -> None:
    question = crud.create_question_db(session, question_create)
    answer = crud.create_answer_db(session, answer_create, question)
    assert session.get(AnswerDB, answer.id)

    crud.delete_answer_db(session, answer)
    assert was_deleted(answer)


def test_get_question_with_answers(
    session: Session,
    question_create: QuestionCreate,
    answer_create: AnswerCreate,
) -> None:
    question = crud.create_question_db(session, question_create)
    answer = crud.create_answer_db(session, answer_create, question)

    question_answers_tuple = crud.get_question_with_answers_db(session, question.id)
    assert len(question_answers_tuple) == 1
    assert question_answers_tuple[0] is answer


def test_is_user_answered_question_db(
    session: Session,
    question_create: QuestionCreate,
    answer_create: AnswerCreate,
    extra_question_create: QuestionCreate,
) -> None:
    question = crud.create_question_db(session, question_create)
    extra_question = crud.create_question_db(session, extra_question_create)
    answer = crud.create_answer_db(session, answer_create, question)

    is_answered = crud.is_user_answered_question_db(
        session, answer.user_id, question.id
    )
    assert is_answered

    is_answered = crud.is_user_answered_question_db(
        session, answer.user_id, extra_question.id
    )
    assert not is_answered


# Test crud from app.deps.py
def test_get_question_db(session: Session, question_create: QuestionCreate) -> None:
    question = crud.create_question_db(session, question_create)
    question_query = get_question_db(session, question.id)
    assert question is question_query


def test_get_answer_db(
    session, question_create: QuestionCreate, answer_create: AnswerCreate
) -> None:
    question = crud.create_question_db(session, question_create)
    answer = crud.create_answer_db(session, answer_create, question)

    answer_query = get_answer_db(session, answer.id)
    assert answer is answer_query
