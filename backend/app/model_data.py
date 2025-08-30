from datetime import datetime

from pydantic import BaseModel, TypeAdapter


TupleQuestions = TypeAdapter(tuple["Question", ...])
TupleAnswers = TypeAdapter(tuple["Answer", ...])


# TODO: what kind of validation do I need?! Task expects to check if str isn't empty. But... I have no boundaries for those fields int the same task. If everyone will set up it's own boundaries it will be such a mess...
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


# Need if TupleAnswer was defined before inner classes
# https://docs.pydantic.dev/2.11/errors/usage_errors/#class-not-fully-defined
TupleAnswers.rebuild()
