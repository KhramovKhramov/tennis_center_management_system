"""Фикстуры пользователей."""

import pytest_asyncio

from src.models import User
from tests.factories.user import UserFactory


@pytest_asyncio.fixture(scope='function')
async def user(test_session) -> User:
    """Фикстура, возвращающая объект пользователя."""

    user = UserFactory.build()

    test_session.add(user)
    await test_session.commit()

    return user


@pytest_asyncio.fixture(scope='function')
async def users(test_session) -> list[User]:
    """Фикстура, возвращающая список объектов пользователей."""

    users = UserFactory.build_batch(5)

    test_session.add_all(users)
    await test_session.commit()

    return users
