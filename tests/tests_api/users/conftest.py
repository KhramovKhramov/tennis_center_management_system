import pytest
from apps.users.models import User

from tests.factories import UserFactory
from tests.utils import get_api_url

# Фикстуры urls


@pytest.fixture(scope='session')
def users_list_url() -> str:
    return get_api_url('users', 'list')


# Фикстуры объектов


@pytest.fixture
def user() -> User:
    return UserFactory.create()


@pytest.fixture
def users() -> list[User]:
    return UserFactory.create_batch(5)
