from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session

from app.model_db import Base
from app.config import settings

engine = create_engine(str(settings.DB_URL))


# TODO: add alembic migrations properly
# https://github.com/fastapi/full-stack-fastapi-template/blob/8af907c763c85c38a2dc745792eda741de5384bb/backend/app/core/db.py#L15
def init_db(engine: Engine) -> None:
    Base.metadata.create_all(engine)


init_db(engine)
