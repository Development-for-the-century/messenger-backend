from typing import Literal

from pydantic import Field, PostgresDsn, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="DB__",
    )
    DSN: PostgresDsn
    SCHEMA: str = "messenger"


class JWTSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="JWT__",
    )
    secret_key: SecretStr
    algorithm: str = Field("HS256")
    cookie_name: str = Field("access_token")
    secure: bool = Field(True)
    samesite: Literal["strict", "lax", "none"] = Field("strict")


def get_db_settings() -> DatabaseSettings:
    return DatabaseSettings()  # pyright: ignore[reportCallIssue]


def get_jwt_settings():
    return JWTSettings()  # pyright: ignore[reportCallIssue]
