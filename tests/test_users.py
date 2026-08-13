from data.users import (
    CREATE_USER_PAYLOAD,
    PARTIAL_USER_PAYLOAD,
    UPDATE_USER_PAYLOAD,
)
from utils.validators import assert_response_time, assert_user_structure


def test_get_users(api_client):
    response = api_client.users.get_users()

    assert response.status_code == 200
    assert_response_time(response)

    data = response.json()

    assert "users" in data
    assert "total" in data
    assert "skip" in data
    assert "limit" in data

    assert isinstance(data["users"], list)
    assert isinstance(data["total"], int)
    assert isinstance(data["skip"], int)
    assert isinstance(data["limit"], int)

    assert_user_structure(data["users"][0])


def test_success_get_user_by_id(api_client):
    user_id = 1
    response = api_client.users.get_user(user_id)

    assert response.status_code == 200
    assert_response_time(response)

    data = response.json()

    assert data["id"] == user_id
    assert_user_structure(data)


def test_failed_get_user_by_id(api_client):
    user_id = 999
    response = api_client.users.get_user(user_id)

    assert response.status_code == 404
    assert_response_time(response)


def test_success_create_user(api_client):
    response = api_client.users.create_user(CREATE_USER_PAYLOAD)

    assert response.status_code == 201
    assert_response_time(response)

    data = response.json()

    assert data["firstName"] == CREATE_USER_PAYLOAD["firstName"]
    assert data["lastName"] == CREATE_USER_PAYLOAD["lastName"]
    assert data["email"] == CREATE_USER_PAYLOAD["email"]
    assert isinstance(data["id"], int)


def test_success_update_user(api_client):
    user_id = 5
    response = api_client.users.update_user(user_id, UPDATE_USER_PAYLOAD)

    assert response.status_code == 200
    assert_response_time(response)

    data = response.json()

    assert data["id"] == user_id
    assert data["firstName"] == UPDATE_USER_PAYLOAD["firstName"]
    assert data["lastName"] == UPDATE_USER_PAYLOAD["lastName"]
    assert data["email"] == UPDATE_USER_PAYLOAD["email"]
    assert_user_structure(data)


def test_success_patch_user(api_client):
    user_id = 5
    response = api_client.users.patch_user(user_id, PARTIAL_USER_PAYLOAD)

    assert response.status_code == 200
    assert_response_time(response)

    data = response.json()

    assert data["id"] == user_id
    assert data["email"] == PARTIAL_USER_PAYLOAD["email"]
    assert_user_structure(data)


def test_success_delete_user(api_client):
    user_id = 5
    response = api_client.users.delete_user(user_id)

    assert response.status_code == 200
    assert_response_time(response)

    data = response.json()

    assert data["id"] == user_id
    assert data["isDeleted"] is True
