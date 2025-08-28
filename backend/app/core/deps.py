from typing import Annotated, TypeAlias, Generator
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.db import engine


def create_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SessionDep: TypeAlias = Annotated[Session, Depends(create_session)]
