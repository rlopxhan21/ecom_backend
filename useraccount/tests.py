import pytest
import json

pytestmark = pytest.mark.django_db


def test_token_create_without_sending_email_and_password_should_throw_error(client) -> None:
    response = client.post(path="/auth/token-create/", data={})
    content = json.loads(response.content)

    assert content == {"email": ["This field is required."], "password": [
        "This field is required."]}
    assert response.status_code == 400


def test_token_create_sending_wrong_email_and_wrong_password_should_throw_error(client) -> None:
    response = client.post(path=("/auth/token-create/"),
                           data={"email": "admin@admin.com", "password": 'admin'})
    content = json.loads(response.content)

    assert content == {
        "detail": "No active account found with the given credentials"}
    assert response.status_code == 401
