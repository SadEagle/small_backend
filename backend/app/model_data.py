from datetime import datetime

from pydantic import BaseModel, TypeAdapter

TupleQuestions = TypeAdapter(tuple["Question", ...])
TupleAnswers = TypeAdapter(tuple["Answer", ...])


class AnswerCreate(BaseModel):
    text: str
    user_id: str


class Answer(AnswerCreate):
    id: int
    created_at: datetime


class QuestionCreate(BaseModel):
    text: str


class Question(QuestionCreate):
    id: int
    create_at: datetime


class QuestionWithAnswers(BaseModel):
    question: Question
    answers: tuple[Answer, ...]


class Message(BaseModel):
    message: str
