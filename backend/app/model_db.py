from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, func


class Base(DeclarativeBase):
    pass


class QuestionDB(Base):
    __tablename__ = "question"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    # TODO: recheck cascade one more time
    # https://docs.sqlalchemy.org/en/14/orm/cascades.html
    answers: Mapped[list["AnswerDB"]] = relationship(
        back_populates="question", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return (
            f"QuestionDB(id={self.id}, text='{self.text}', create_at={self.create_at})"
        )


class AnswerDB(Base):
    __tablename__ = "answer"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    user_id: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    question_id: Mapped[int] = mapped_column(ForeignKey("question.id"))
    question: Mapped[QuestionDB] = relationship(back_populates="answers")

    def __repr__(self) -> str:
        return f"AnswerDB(id={self.id}, text='{self.text}', user_id='{self.user_id}', create_at={self.create_at}, question_id={self.question_id})"
