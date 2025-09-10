from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.model_db import AnswerDB, QuestionDB
from app.model_data import AnswerCreate, QuestionCreate


async def create_question_db(
    session: AsyncSession, question_create: QuestionCreate
) -> QuestionDB:
    question_dict = question_create.model_dump(mode="json")
    question = QuestionDB(**question_dict)
    session.add(question)
    await session.commit()
    # Skip loading answers relation
    await session.refresh(question, ["id", "created_at"])
    return question


async def delete_question_db(session: AsyncSession, question: QuestionDB) -> None:
    await session.delete(question)
    await session.commit()


async def create_answer_db(
    session: AsyncSession, answer_create: AnswerCreate, target_question: QuestionDB
) -> AnswerDB:
    answer_dict = answer_create.model_dump(mode="json")
    answer = AnswerDB(**answer_dict)
    answer.question = target_question

    session.add(answer)
    await session.commit()
    await session.refresh(answer, ["id", "created_at"])
    return answer


async def delete_answer_db(session: AsyncSession, answer: AnswerDB) -> None:
    await session.delete(answer)
    await session.commit()


async def get_all_questions_db(session: AsyncSession) -> tuple[QuestionDB, ...]:
    statement = select(QuestionDB)
    questions_tuple = (await session.scalars(statement)).all()
    return tuple(questions_tuple)


async def get_question_with_answers_db(
    session: AsyncSession, question_id: int
) -> tuple[AnswerDB, ...]:
    statement = select(AnswerDB).where(AnswerDB.question_id == question_id)
    answers_tuple = (await session.scalars(statement)).all()
    return tuple(answers_tuple)


async def is_user_answered_question_db(
    session: AsyncSession, user_id: str, question_id: int
) -> bool:
    """Check if user already answered certain question

    Args:
        session: orm session
        user_id: user id
        question_id: question id

    Returns:
        True - if user already answered, False otherwise
    """
    statement = (
        select(AnswerDB)
        .where(AnswerDB.question_id == question_id)
        .where(AnswerDB.user_id == user_id)
    )
    current_user_answer = await session.scalar(statement)
    return current_user_answer is not None
