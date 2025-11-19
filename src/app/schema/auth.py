from pydantic import BaseModel, SecretStr


class LoginForm(BaseModel):
    username: str
    password: SecretStr


class Token(BaseModel):
    access_token: str


class LogoutOK(BaseModel):
    detail: str = "Log out"
