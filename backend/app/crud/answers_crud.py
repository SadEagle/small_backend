from sqlalchemy.orm import Session

from app.data_models.answers_model import Answer, AnswerOutConfirm


def get_answer_db(session: Session, answer_id: int) -> Answer:
    pass


def delete_answer_db(session: Session, answer_id: int) -> AnswerOutConfirm:
    pass
