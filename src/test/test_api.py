from fastapi import status
from fastapi.testclient import TestClient


def test_api_login_authorized(test_client: TestClient) -> None:
    response = test_client.post(
        "/api/auth/token",
        data={"username": "name", "password": "fkjhKJHfkIOF"},
    )

    assert response.status_code == status.HTTP_200_OK
    json_response = response.json()
    assert "access_token" in json_response


def test_api_get_me_authorized(test_client: TestClient) -> None:
    login_response = test_client.post(
        "/api/auth/token",
        data={"username": "name", "password": "fkjhKJHfkIOF"},
    )
    assert login_response.status_code == status.HTTP_200_OK
    token_data = login_response.json()
    access_token = token_data["access_token"]

    response = test_client.get(
        "/api/auth/me", headers={"Authorization": f"Bearer {access_token}"}
    )

    assert response.status_code == status.HTTP_200_OK
    json_response = response.json()
    assert json_response == {"username": "name"}


def test_api_logout(test_client: TestClient) -> None:
    response = test_client.post("/api/auth/logout")

    assert response.status_code == status.HTTP_200_OK
    json_response = response.json()
    assert json_response == {"detail": "Log out"}


def test_api_get_me_unauthorized(test_client: TestClient) -> None:
    response = test_client.get("/api/auth/me")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    json_response = response.json()
    assert json_response == {"error": "Unauthorized"}
