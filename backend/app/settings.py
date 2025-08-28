from enum import StrEnum

from pydantic_settings import BaseSettings, SettingsConfigDict


class RunMode(StrEnum):
    PROD = "prod"
    DEV = "dev"
    TEST = "test"


class Settings(BaseSettings):
    # TODO: add .env file
    # model_config = SettingsConfigDict(
    #     env_file=".env",
    #     extra="ignore",
    # )

    PROD_DB_URL = "sqlite:///:memory:"
    DEV_DB_URL = "sqlite:///:memory:"
    TEST_DB_URL = "sqlite:///:memory:"
    RUN_MODE: RunMode = RunMode.DEV


settings = Settings()
