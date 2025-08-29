from enum import StrEnum

from pydantic_settings import BaseSettings, SettingsConfigDict


class RunMode(StrEnum):
    PROD = "prod"
    DEV = "dev"
    TEST = "test"


# TODO: make proper settings with .env file pinned inside
class Settings(BaseSettings):
    # TODO: add .env file
    # model_config = SettingsConfigDict(
    #     env_file=".env",
    #     extra="ignore",
    # )

    RUN_MODE: RunMode = RunMode.DEV
    # PROD_DB_URL: str = "sqlite:///:memory:"
    # DEV_DB_URL: str = "sqlite:///:memory:"
    DEV_DB_URL: str = "sqlite:///test.db"
    TEST_DB_URL: str = "sqlite:///test.db"


settings = Settings()
