from sqlalchemy import create_engine

from app.settings import settings, RunMode
from app.model_db import Base

# TODO: make init db and init tables as distinct function?!
if settings.RUN_MODE == RunMode.DEV:
    engine = create_engine(settings.DEV_DB_URL, echo=True)
elif settings.RUN_MODE == RunMode.PROD:
    engine = create_engine(settings.PROD_DB_URL)
else:
    engine = create_engine(settings.TEST_DB_URL)

Base.metadata.create_all(engine)
