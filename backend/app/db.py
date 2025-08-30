from sqlalchemy import create_engine

from app.model_db import Base
from app.settings import settings


engine = create_engine(settings.DB_URL)


# TODO: add alembic migrations properly
# https://github.com/fastapi/full-stack-fastapi-template/blob/8af907c763c85c38a2dc745792eda741de5384bb/backend/app/core/db.py#L15
Base.metadata.create_all(engine)
