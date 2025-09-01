import os
from pydantic import computed_field, PostgresDsn
from pydantic_settings import BaseSettings


# TODO: replace db_url with postgres one
# Also, do i need to make pytest calls without postgres params? Probably, make shell script with random initialization?!
class Settings(BaseSettings):
    POSTGRES_SERVER: str
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str = ""
    POSTGRES_DB: str = ""

    TEST_DB_URL: str = "sqlite:///./test.db"

    @computed_field
    @property
    def DB_URL(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql+psycopg2",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )


settings = Settings()  # type: ignore
