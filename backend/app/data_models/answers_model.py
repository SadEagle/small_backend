from datetime import datetime
from pydantic import BaseModel, TypeAdapter


ListAnswers: TypeAdapter = TypeAdapter(list["Answer"])


class AnswerCreate(BaseModel):
    user_id: str
    text: str
    created_at: datetime


class Answer(AnswerCreate):
    id: int


class AnswerOutConfirm(BaseModel):
    id: int
