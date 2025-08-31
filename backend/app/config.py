from pydantic_settings import BaseSettings


# TODO: generate url as computed field for postgres
# But... how do i handle test with sqlite then?
class Settings(BaseSettings):
    DB_URL: str = "sqlite:///dev.db"
    TEST_DB_URL: str = "sqlite:///./dev.db"


settings = Settings()
