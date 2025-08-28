from datetime import datetime

from pydantic import BaseModel, TypeAdapter

from app.data_models.answers_model import Answer

ListQuestions: TypeAdapter = TypeAdapter(list["Question"])
ListQuestionWithAnswers: TypeAdapter = TypeAdapter(list["QuestionWithAnswers"])


class QuestionCreate(BaseModel):
    text: str


class Question(QuestionCreate):
    id: int
    created_at: datetime


class QuestionOutConfirm(BaseModel):
    id: int


class QuestionWithAnswers(BaseModel):
    question: Question
    answers: list[Answer]
