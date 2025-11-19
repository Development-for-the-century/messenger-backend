import uuid

from fastapi import Response
from jwt import encode

from app.config import JWTSettings
from app.exception import Api400Error
from app.schema.auth import LoginForm, LogoutOK, Token
from app.schema.user import UserInfo, UserJWTBody

jwt_settings = JWTSettings()  # type: ignore


async def get_jwt_token(form_data: LoginForm, response: Response) -> Token:
    try:
        if not form_data.username or not form_data.password.get_secret_value():
            raise Api400Error(message="Invalid credentials")

        user = UserInfo(username=form_data.username)

        payload = UserJWTBody(
            field_name=user.username,
            field_value=uuid.uuid4(),
        ).model_dump(mode="json")

        token = encode(
            payload,
            jwt_settings.secret_key.get_secret_value(),
            algorithm=jwt_settings.algorithm,
        )

        response.set_cookie(
            key=jwt_settings.cookie_name,
            value=token,
            httponly=True,
            secure=jwt_settings.secure,
            samesite=jwt_settings.samesite,
        )

        return Token(access_token=token)

    except Exception as exception:
        raise Api400Error(message=f"Login failed: {str(exception)}") from exception


async def remove_access_token(response: Response) -> LogoutOK:
    response.delete_cookie(
        key=jwt_settings.cookie_name,
    )
    return LogoutOK()
