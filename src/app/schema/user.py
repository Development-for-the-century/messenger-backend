from uuid import UUID

from pydantic import BaseModel


class UserInfo(BaseModel):
    username: str


class UserJWTBody(BaseModel):
    field_name: str
    field_value: UUID
