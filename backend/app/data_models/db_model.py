from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, func


class Base(DeclarativeBase):
    pass


class Question(Base):
    __tablename__ = "question"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    create_at: Mapped[datetime] = mapped_column(server_default=func.now())

    answers: Mapped[list["Answer"]] = relationship(back_populates="answer")


class Answer(Base):
    __tablename__ = "answer"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    create_at: Mapped[datetime] = mapped_column(server_default=func.now())

    question_id: Mapped[int] = mapped_column(ForeignKey("question.id"))
    question: Mapped[Question] = relationship(back_populates="question")
