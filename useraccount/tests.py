import pytest
import json

from useraccount.models import CustomUser

pytestmark = pytest.mark.django_db

# ------------------------- Fixtures & Used Variables ------------------------ #

email = "admin@admin.com"
password = "admin"


@pytest.fixture
def create_normal_user():
    return CustomUser.objects.create_user(email=email, password=password, full_name="admin admin", is_active=True, is_staff=False, is_superuser=False)


@pytest.fixture
def create_token(client, create_normal_user):
    response = client.post(path='/auth/token-create/',
                           data={"email": email, "password": password})
    content = json.loads(response.content)

    return content


@pytest.fixture
def get_expired_refresh_token(client, create_token):
    expired_token = create_token['refresh']
    client.post(path='/auth/token-blacklist/',
                data={"refresh": expired_token})

    return expired_token


# ------------------ Testing .../auth/token-create/ endpoint ----------------- #


def test_token_create_without_sending_email_and_password_should_throw_error(client) -> None:
    response = client.post(path="/auth/token-create/", data={})
    content = json.loads(response.content)

    assert content == {"email": ["This field is required."], "password": [
        "This field is required."]}
    assert response.status_code == 400


def test_token_create_sending_wrong_email_and_wrong_password_should_throw_error(client) -> None:
    response = client.post(path=("/auth/token-create/"),
                           data={"email": email, "password": password})
    content = json.loads(response.content)

    assert content == {
        "detail": "No active account found with the given credentials"}
    assert response.status_code == 401


def test_token_create_with_correct_email_and_password(client, create_normal_user) -> None:
    response = client.post(path='/auth/token-create/',
                           data={"email": email, "password": password})
    content = json.loads(response.content)

    assert "access" in content
    assert "refresh" in content
    assert response.status_code == 200


# ------------------ Testing .../auth/token-refresh endpoint ----------------- #

def test_token_refresh_without_sending_refresh_token(client) -> None:
    response = client.post(path="/auth/token-refresh/", data={})
    content = json.loads(response.content)

    assert content == {'refresh': ['This field is required.']}
    assert response.status_code == 400


def test_token_refresh_sending_not_a_token(client) -> None:
    response = client.post(path="/auth/token-refresh/",
                           data={"refresh": "notarefreshtoken"})
    content = json.loads(response.content)

    assert content == {'code': 'token_not_valid',
                       'detail': 'Token is invalid or expired'}
    assert response.status_code == 401


def test_token_refresh_sending_access_token(client, create_token) -> None:
    response = client.post(path="/auth/token-refresh/",
                           data={"refresh": create_token['access']})
    content = json.loads(response.content)

    assert content == {'code': 'token_not_valid',
                       'detail': 'Token has wrong type'}
    assert response.status_code == 401


def test_token_refresh_sending_expired_refresh_token(client, get_expired_refresh_token) -> None:
    response = client.post(path="/auth/token-refresh/",
                           data={"refresh": get_expired_refresh_token})
    content = json.loads(response.content)

    assert content == {'code': 'token_not_valid',
                       'detail': 'Token is blacklisted'}
    assert response.status_code == 401


def test_token_refresh_sending_refresh_token(client, create_token) -> None:
    response = client.post(path="/auth/token-refresh/",
                           data={"refresh": create_token['refresh']})
    content = json.loads(response.content)

    assert "access" in content
    assert "refresh" in content
    assert response.status_code == 200

# ----------------- Testing .../auth/token-blacklist endpoint ---------------- #

# -------------------- Testing .../auth/register endpoint -------------------- #
