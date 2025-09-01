from fastapi import APIRouter, HTTPException, status

from app import crud
from app.deps import CurrentQuestionDep, SessionDep
from app.model_data import (
    AnswerCreate,
    Question,
    QuestionCreate,
    QuestionWithAnswers,
    TupleAnswers,
    TupleQuestions,
    Message,
)


app_questions = APIRouter(prefix="/questions")


@app_questions.get("/")
def get_all_questions(session: SessionDep) -> tuple[Question, ...]:
    questions_list = crud.get_all_questions_db(session)
    return TupleQuestions.validate_python(questions_list, from_attributes=True)


@app_questions.post("/", status_code=status.HTTP_201_CREATED)
def create_question(
    session: SessionDep,
    question: QuestionCreate,
) -> Message:
    crud.create_question_db(session, question)
    return Message(message="Question was succesfully created")


@app_questions.get("/{question_id}")
def get_question_with_answers(
    session: SessionDep, current_question: CurrentQuestionDep
) -> QuestionWithAnswers:
    answers_tuple = crud.get_question_with_answers_db(session, current_question.id)
    question = Question.model_validate(current_question, from_attributes=True)
    answers = TupleAnswers.validate_python(answers_tuple, from_attributes=True)
    return QuestionWithAnswers(question=question, answers=answers)


@app_questions.delete("/{question_id}")
def delete_question(
    session: SessionDep, current_question: CurrentQuestionDep
) -> Message:
    crud.delete_question_db(session, current_question)
    return Message(message="Question was succesfully deleted")


@app_questions.post(
    "/{question_id}/answers",
    status_code=status.HTTP_201_CREATED,
)
def create_answer(
    session: SessionDep,
    target_question: CurrentQuestionDep,
    answer_create: AnswerCreate,
) -> Message:
    # if crud.is_user_answered_question_db(
    #     session, answer_create.user_id, target_question.id
    # ):
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail="Can't create answer. User already answered current question",
    #     )
    crud.create_answer_db(session, answer_create, target_question)
    return Message(message="Answer was succesfully created")
