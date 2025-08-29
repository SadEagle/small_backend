from fastapi import APIRouter, HTTPException, status

from app.crud import (
    get_all_questions_db,
    get_question_answers_db,
    is_user_answered_question_db,
)
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
from app.model_db import QuestionDB, AnswerDB


app_questions = APIRouter(prefix="/questions")


@app_questions.get("/")
def get_all_questions(session: SessionDep) -> tuple[Question, ...]:
    questions_list = get_all_questions_db(session)
    return TupleQuestions.validate_python(questions_list, from_attributes=True)


@app_questions.get("/{question_id}")
def get_question_with_answers(
    session: SessionDep, current_question: CurrentQuestionDep
) -> QuestionWithAnswers:
    answers_tuple = get_question_answers_db(session, current_question.id)
    question = Question.model_validate(current_question, from_attributes=True)
    answers = TupleAnswers.validate_python(answers_tuple, from_attributes=True)
    return QuestionWithAnswers(question=question, answers=answers)


@app_questions.post("/{question_id}", status_code=status.HTTP_201_CREATED)
def create_questions(
    session: SessionDep,
    question: QuestionCreate,
) -> Message:
    question_dict = question.model_dump(mode="json")
    session.add(QuestionDB(**question_dict))
    session.commit()
    return Message(message="Question was succesfully created")


@app_questions.delete("/{question_id}")
def delete_id_question(
    session: SessionDep, current_question: CurrentQuestionDep
) -> Message:
    session.delete(current_question)
    session.commit()
    return Message(message="Question was succesfully deleted")


@app_questions.post(
    "/{question_id}/answers",
    status_code=status.HTTP_201_CREATED,
)
def create_answer_id_question(
    session: SessionDep,
    target_question: CurrentQuestionDep,
    answer_create: AnswerCreate,
) -> Message:
    if is_user_answered_question_db(session, answer_create.user_id, target_question.id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Can't create answer. User already answered current question",
        )
    answer_dict = answer_create.model_dump(mode="json")
    answer = AnswerDB(**answer_dict)
    target_question.answers.append(answer)
    session.commit()
    return Message(message="Answer was succesfully created")
