"""Тесты API пользователей."""

from datetime import datetime

import pytest
from fastapi import status

from src.models import User
from tests.core.urls_config import USERS_API_URL
from tests.helpers.user import (
    create_user_request_data,
    serialize_user,
    update_user_request_data,
)


@pytest.mark.asyncio
async def test_create_user(unauthorized_client, test_session):
    """
    Тест создания пользователя.

    Ожидание: статус 201 в ответе, пользователь сохраняется в БД.
    В ответе на запрос возвращается сохраненный объект в ожидаемом формате.
    """

    response = await unauthorized_client.post(
        USERS_API_URL,
        json=await create_user_request_data(),
    )
    assert response.status_code == status.HTTP_201_CREATED

    response_data = response.json()
    instance = await test_session.get(User, response_data['id'])
    assert response_data == await serialize_user(instance)


@pytest.mark.asyncio
async def test_get_user_by_id(unauthorized_client, user):
    """
    Тест получения данных пользователя по идентификатору.

    Ожидание: статус 200 в ответе, возвращается объект из БД в ожидаемом
    формате.
    """

    response = await unauthorized_client.get(f'{USERS_API_URL}{user.id}/')
    assert response.status_code == status.HTTP_200_OK
    response_data = response.json()

    assert response_data == await serialize_user(user)


@pytest.mark.asyncio
async def test_get_users_list(unauthorized_client, users):
    """
    Тест получения списка пользователей.

    Ожидание: статус 200 в ответе, возвращается список объектов из БД
    в ожидаемом формате.
    """

    response = await unauthorized_client.get(USERS_API_URL)
    assert response.status_code == status.HTTP_200_OK

    response_data = response.json()
    assert len(response_data) == len(users)

    assert response_data[0] == await serialize_user(users[0])


@pytest.mark.asyncio
async def test_update_user(unauthorized_client, user):
    """
    Тест обновления данных пользователя.

    Ожидание: статус 200 в ответе, возвращается обновленный объект из БД
    в ожидаемом формате.
    """

    update_data = await update_user_request_data()

    response = await unauthorized_client.patch(
        f'{USERS_API_URL}{user.id}/',
        json=update_data,
    )

    assert response.status_code == status.HTTP_200_OK
    response_data = response.json()

    assert response_data == await serialize_user(user)
    for key, value in update_data.items():
        assert (
            getattr(user, key) == datetime.strptime(value, '%Y-%m-%d').date()
            if key == 'date_of_birth'
            else value
        )


@pytest.mark.asyncio
async def test_delete_user(unauthorized_client, test_session, user):
    """
    Тест удаления пользователя.

    Ожидание: статус 204 в ответе, объект удален из БД.
    """

    response = await unauthorized_client.delete(f'{USERS_API_URL}{user.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT

    deleted_user = await test_session.get(User, user.id)
    assert not deleted_user
