from typing import Annotated

from fastapi import APIRouter, Depends, Form, Response

from app.schema.auth import LoginForm, LogoutOK, Token
from app.schema.user import UserInfo, UserJWTBody
from app.service.auth.decorator import current_user_requierd
from app.service.auth.jwt_token import get_jwt_token, remove_access_token

router = APIRouter(tags=["Authorization"], prefix="/auth")


@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[LoginForm, Form()],
    response: Response,
) -> Token:
    return await get_jwt_token(form_data=form_data, response=response)


@router.post("/logout")
async def logout(response: Response) -> LogoutOK:
    return await remove_access_token(response=response)


@router.get("/me")
async def get_me(
    user: Annotated[UserJWTBody, Depends(current_user_requierd)],
) -> UserInfo:
    return UserInfo(username=user.field_name)
