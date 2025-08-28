from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, func


class Base(DeclarativeBase):
    pass


class QuestionDB(Base):
    __tablename__ = "question"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    create_at: Mapped[datetime] = mapped_column(server_default=func.now())

    answers: Mapped[list["AnswerDB"]] = relationship(back_populates="answer")

    def __repr__(self) -> str:
        return f"Question(id={self.id}, text='{self.text}', create_at={self.create_at})"


class AnswerDB(Base):
    __tablename__ = "answer"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    create_at: Mapped[datetime] = mapped_column(server_default=func.now())

    question_id: Mapped[int] = mapped_column(ForeignKey("question.id"))
    question: Mapped[QuestionDB] = relationship(back_populates="question")

    def __repr__(self) -> str:
        return f"Answer(id={self.id}, text='{self.text}', create_at={self.create_at})"
