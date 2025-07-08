from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import FileUrl, IPvAnyAddress, HttpUrl

__all__ = ["config"]


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False, extra="ignore"
    )

    SCRIPT_PATH: FileUrl
    TOKEN: str
    ADMIN_ID: int
    WEB_SERVER_HOST: IPvAnyAddress
    WEB_SERVER_PORT: int
    WEBHOOK_PATH: str
    WEBHOOK_SECRET: str
    BASE_WEBHOOK_URL: HttpUrl


config = Config()
