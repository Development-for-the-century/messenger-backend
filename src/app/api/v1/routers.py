from fastapi import APIRouter, Depends, HTTPException, Response

from app.config import config, security
from app.schema.auth import UserLoginSchema

router = APIRouter(tags=["Authorization"])


@router.post("/login")
def login(creds: UserLoginSchema, response: Response):
    if creds.username == "uname" and creds.password == "test":
        token = security.create_access_token(uid="123")
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Incorrect username or password")


@router.get("/protected", dependencies=[Depends(security.access_token_required)])
def protected():
    return {"data": "Protected data"}
