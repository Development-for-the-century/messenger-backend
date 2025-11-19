from typing import Literal

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class JWTSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="JWT__",
        env_file=[".env.test", ".env"],
        env_file_encoding="utf-8",
    )
    secret_key: SecretStr
    algorithm: str = Field("HS256")
    cookie_name: str = Field("access_token")
    secure: bool = Field(True)
    samesite: Literal["strict", "lax", "none"] = Field("strict")


def get_jwt_settings():
    return JWTSettings()  # type: ignore
