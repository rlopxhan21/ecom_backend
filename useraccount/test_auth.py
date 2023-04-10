# # from django.urls import reverse
# import pytest
# import json


# from useraccount.models import CustomUser

# pytestmark = pytest.mark.django_db

# @pytest.fixture
# def create_normal_user():
#     return CustomUser.objects.create_user(email="admin@admin.com", password="admin", full_name="Admin")

# def test_user_auth_without_argument_should_raise_error(client, create_normal_user) -> None:
#     response = client.post(path=('/auth/token-create/'), data={})
#     content = json.loads(response.content)

#     assert response.status_code == 400
#     assert {"email":["This field is required."],"password":["This field is required."]} == content


