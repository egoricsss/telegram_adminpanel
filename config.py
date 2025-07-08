from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import FileUrl

__all__ = ["config"]


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False, extra="ignore"
    )

    SCRIPT_PATH: FileUrl
    TOKEN: str
    ADMIN_ID: int


config = Config()
