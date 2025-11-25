from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer

from app.api.v1.routers import router as v1_router
from app.exception import Api500Error, BaseAPIError
from db.api import router as db_router

token_auth_svheme = HTTPBearer()

app = FastAPI()

router = APIRouter(prefix="/api")
router.include_router(v1_router)
router.include_router(db_router)
app.include_router(router=router)


@app.exception_handler(BaseAPIError)
async def base_api_error(
    _request: Request,
    exc: BaseAPIError,
) -> JSONResponse:
    return exc.response


@app.exception_handler(Exception)
async def base_exception_callback(
    _request: Request,
    exc: Exception,
) -> JSONResponse:
    return Api500Error(message=f"Something get wrong: {exc!s}").response
