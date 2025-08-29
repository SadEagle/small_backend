from sqlalchemy import create_engine

from app.settings import settings, RunMode
from app.model_db import Base

if settings.RUN_MODE == RunMode.DEV:
    engine = create_engine(settings.DEV_DB_URL, echo=True)
elif settings.RUN_MODE == RunMode.PROD:
    engine = create_engine(settings.PROD_DB_URL)
else:
    engine = create_engine(settings.TEST_DB_URL)

# TODO: decide where to place talbe generations. Expect that it will be better to move it into app.model_db, where we init them
Base.metadata.create_all(engine)
