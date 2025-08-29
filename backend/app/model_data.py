from datetime import datetime

from pydantic import BaseModel, TypeAdapter

TupleQuestions = TypeAdapter(tuple["Question", ...])
TupleAnswers = TypeAdapter(tuple["Answer", ...])


class AnswerCreate(BaseModel):
    text: str
    user_id: str


class Answer(AnswerCreate):
    id: int
    question_id: int
    created_at: datetime


class QuestionCreate(BaseModel):
    text: str


class Question(QuestionCreate):
    id: int
    created_at: datetime


class QuestionWithAnswers(BaseModel):
    question: Question
    answers: tuple[Answer, ...]


class Message(BaseModel):
    message: str


# https://docs.pydantic.dev/2.11/errors/usage_errors/#class-not-fully-defined
TupleAnswers.rebuild()
