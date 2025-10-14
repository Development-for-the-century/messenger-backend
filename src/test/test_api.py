from fastapi import status
from fastapi.testclient import TestClient
import pytest
from authx.exceptions import MissingTokenError


def test_api_protected_success(test_client: TestClient) -> None:
    with pytest.raises(MissingTokenError):
        test_client.get("/api/protected")


def test_api_login_unauthorized(test_client: TestClient) -> None:
    response = test_client.post(
        "/api/login",
        json={"username": "", "password": ""},
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_api_login_authorized(test_client: TestClient) -> None:
    response = test_client.post(
        "/api/login",
        json={"username": "uname", "password": "test"},
    )

    assert response.status_code == status.HTTP_200_OK
    json_response = response.json()
    assert json_response == {"access_token": json_response["access_token"]}


def test_api_protected_authorized(test_client: TestClient) -> None:
    response = test_client.get("/api/protected")

    assert response.status_code == status.HTTP_200_OK
    json_response = response.json()
    assert json_response == {"data": "Protected data"}
