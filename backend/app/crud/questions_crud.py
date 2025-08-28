from sqlalchemy.orm import Session

from app.data_models.questions_model import (
    Question,
    QuestionCreate,
    QuestionOutConfirm,
    QuestionWithAnswers,
)


def get_all_questions_db(session: Session) -> list[Question]:
    pass


def create_question_db(
    session: Session, question: QuestionCreate
) -> QuestionOutConfirm:
    pass


def get_question_db(session: Session, question_id: int) -> Question:
    pass


def delete_question_db(session: Session, question_id) -> QuestionOutConfirm:
    pass


def get_question_with_answers_db(
    session: Session, question_id: int
) -> QuestionWithAnswers:
    pass
