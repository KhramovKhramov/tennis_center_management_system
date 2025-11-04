import pytest
from apps.user.models import User
from rest_framework import status

from tests.helpers.user.user import (
    get_create_user_request_data_all_fields,
    get_create_user_request_data_only_required_fields,
    get_update_user_request_data,
    serialize_user,
)
from tests.utils import get_api_url

# Базовые тесты (CRUD, количество запросов, пагинация)


@pytest.mark.django_db
def test_user_create(unauthorized_client, users_list_url):
    """Тест создания пользователя со всеми полями и только обязательными."""

    request_data = [
        get_create_user_request_data_only_required_fields(),
        get_create_user_request_data_all_fields(),
    ]

    for data in request_data:
        response = unauthorized_client.post(users_list_url, data=data)
        assert response.status_code == status.HTTP_201_CREATED

        instance = User.objects.get(pk=response.data['id'])
        assert response.data == serialize_user(instance)


@pytest.mark.django_db
def test_user_update(unauthorized_client, user):
    """Тест обновления данных пользователя."""

    request_data = get_update_user_request_data()

    response = unauthorized_client.patch(
        get_api_url('users', 'detail', pk=user.pk), data=request_data
    )
    assert response.status_code == status.HTTP_200_OK

    user.refresh_from_db()
    assert response.data == serialize_user(user)

    for key, value in request_data.items():
        assert getattr(user, key) == value


@pytest.mark.django_db
def test_user_delete(unauthorized_client, user):
    """Тест удаления пользователя."""

    response = unauthorized_client.delete(
        get_api_url('users', 'detail', pk=user.pk)
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT

    assert not User.objects.filter(pk=user.pk).exists()


@pytest.mark.django_db
def test_user_retrieve(unauthorized_client, user):
    """Тест получения данных пользователя по идентификатору."""

    response = unauthorized_client.get(
        get_api_url('users', 'detail', pk=user.pk)
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.data == serialize_user(user)


@pytest.mark.django_db
def test_users_list(unauthorized_client, users_list_url, users):
    """Тест получения списка пользователей."""

    response = unauthorized_client.get(users_list_url)
    assert response.status_code == status.HTTP_200_OK

    assert response.data[0] == serialize_user(users[-1])


@pytest.mark.django_db
def test_users_list_max_queries(
    unauthorized_client,
    users_list_url,
    users,
    django_assert_max_num_queries,
):
    """
    Тест проверки максимального количество запросов
    в списке пользователей.
    """

    # 1:
    # - основной запрос
    with django_assert_max_num_queries(1):
        response = unauthorized_client.get(users_list_url)
        assert response.status_code == status.HTTP_200_OK
