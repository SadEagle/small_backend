from sqlalchemy import select
from sqlalchemy.orm import Session

from app.model_db import AnswerDB, QuestionDB
from app.model_data import AnswerCreate, QuestionCreate


def create_question_db(session: Session, question_create: QuestionCreate) -> QuestionDB:
    question = QuestionDB(**question_create.model_dump(mode="json"))
    session.add(question)
    session.commit()
    session.refresh(question)
    return question


def delete_question_db(session: Session, question: QuestionDB) -> None:
    session.delete(question)
    session.commit()


def create_answer_db(
    session: Session, answer_create: AnswerCreate, target_question: QuestionDB
) -> AnswerDB:
    answer_dict = answer_create.model_dump(mode="json")
    answer = AnswerDB(**answer_dict)
    target_question.answers.append(answer)
    session.commit()
    session.refresh(answer)
    return answer


def delete_answer_db(session: Session, answer: AnswerDB) -> None:
    session.delete(answer)
    session.commit()


def get_all_questions_db(session: Session) -> tuple[QuestionDB, ...]:
    statement = select(QuestionDB)
    questions_tuple = session.scalars(statement).all()
    return tuple(questions_tuple)


def get_question_with_answers_db(
    session: Session, question_id: int
) -> tuple[AnswerDB, ...]:
    statement = select(AnswerDB).where(AnswerDB.question_id == question_id)
    answers_tuple = session.scalars(statement).all()
    return tuple(answers_tuple)


# def is_user_answered_question_db(
#     session: Session, user_id: str, question_id: int
# ) -> bool:
#     """Check if user already answered certain question
#
#     Args:
#         session: orm session
#         user_id: user id
#         question_id: question id
#
#     Returns:
#         True - if user already answered, False otherwise
#     """
#     statement = (
#         select(AnswerDB)
#         .where(AnswerDB.question_id == question_id)
#         .where(AnswerDB.user_id == user_id)
#     )
#     current_user_answer = session.scalar(statement)
#     return current_user_answer is not None
