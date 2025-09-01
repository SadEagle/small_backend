from sqlalchemy import create_engine

from app.config import settings

engine = create_engine(str(settings.DB_URL))

# NOTE: Tables init via alembic
