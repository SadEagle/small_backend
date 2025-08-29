from sqlalchemy import select
from sqlalchemy.orm import Session

from app.model_db import AnswerDB, QuestionDB


# WARN: slow orm version, bulk will be better if many questions
def get_all_questions_db(session: Session) -> tuple[QuestionDB, ...]:
    statement = select(QuestionDB)
    questions_tuple = session.execute(statement).scalars().all()
    return tuple(questions_tuple)


def get_question_answers_db(session: Session, question_id: int) -> tuple[AnswerDB, ...]:
    statement = select(AnswerDB).where(AnswerDB.question_id == question_id)
    answers_tuple = session.execute(statement).scalars().all()
    return tuple(answers_tuple)


def is_user_answered_question_db(
    session: Session, user_id: str, question_id: int
) -> bool:
    """Check if user already answered certain question

    Args:
        session: orm session
        user_id: user id
        question_id: question id

    Returns:
        True - if user already answered, False otherwise
    """
    statement = (
        select(AnswerDB)
        .where(AnswerDB.question_id == question_id)
        .where(AnswerDB.user_id == user_id)
    )
    current_user_answer = session.execute(statement).one_or_none()
    return current_user_answer is not None
