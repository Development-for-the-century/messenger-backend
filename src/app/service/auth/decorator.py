from typing import Annotated

from fastapi import Security
from fastapi.security import APIKeyCookie, HTTPAuthorizationCredentials, HTTPBearer
from jwt import decode

from app.config import get_jwt_settings
from app.exception import Api400Error, Api401Error
from app.schema.user import UserJWTBody

COOKIE_AUTH_SCHEME = APIKeyCookie(name=get_jwt_settings().cookie_name, auto_error=False)

HEADER_AUTH_SCHEME = HTTPBearer(auto_error=False)


async def current_user_requierd(
    cookie_access_token: Annotated[str | None, Security(COOKIE_AUTH_SCHEME)],
    header_auth: Annotated[
        HTTPAuthorizationCredentials | None, Security(HEADER_AUTH_SCHEME)
    ],
) -> UserJWTBody:
    header_token: str | None = header_auth.credentials if header_auth else None
    access_token: str | None = cookie_access_token or header_token

    if access_token is None:
        raise Api401Error()

    jwt_settings = get_jwt_settings()
    try:
        payload = decode(
            jwt=access_token,
            key=jwt_settings.secret_key.get_secret_value(),
            algorithms=jwt_settings.algorithm,
        )
        return UserJWTBody.model_validate(payload)
    except Exception as exception:
        raise Api400Error() from exception
