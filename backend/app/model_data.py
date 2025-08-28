from datetime import datetime

from pydantic import BaseModel, TypeAdapter

# TODO: check if needed
# ListQuestion = TypeAdapter[list["Question"]]


class AnswerCreate(BaseModel):
    text: str
    question_id: str


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
    answers: list[Answer]


class Message(BaseModel):
    message: str
