import os

from pydantic import computed_field, PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # TODO: need implement test db inisde postgres, probably inside alembic
    POSTGRES_SERVER: str = ""
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = ""
    POSTGRES_PASSWORD: str = ""
    POSTGRES_DB: str = ""

    TEST_DB_URL: str = "sqlite:///./test.db"

    # TODO: make proper pytests, dont understand how to fix this for now
    # Now pytest generate empty file and that's bad practice
    @computed_field
    @property
    def DB_URL(self) -> PostgresDsn | str:
        if os.getenv("PYTEST_VERSION"):
            return "sqlite:///./test.db"
        return PostgresDsn.build(
            scheme="postgresql+psycopg2",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )


settings = Settings()  # type: ignore
