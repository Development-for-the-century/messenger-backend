from starlette import status
from starlette.responses import JSONResponse


class BaseAPIError(Exception):
    _status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    _default_message: str = "Internal service error"

    def __init__(self, message: str | None = None) -> None:
        self.message = message if message else self._default_message
        self.status_code = self._status_code
        super().__init__(self.message)

    @property
    def response(self) -> JSONResponse:
        return JSONResponse(
            status_code=self.status_code,
            content={"error": self.message},
        )


class Api400Error(BaseAPIError):
    _status_code = status.HTTP_400_BAD_REQUEST


class Api404Error(BaseAPIError):
    _status_code = status.HTTP_404_NOT_FOUND


class Api401Error(BaseAPIError):
    _status_code = status.HTTP_401_UNAUTHORIZED
    _default_message = "Unauthorized"


class Api403Error(BaseAPIError):
    _status_code = status.HTTP_403_FORBIDDEN


class Api500Error(BaseAPIError):
    _status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
