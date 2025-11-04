import pytest
from rest_framework.test import APIClient


@pytest.fixture
def unauthorized_client() -> APIClient:
    """Неавторизованный клиент для отправки запросов в тестах."""

    return APIClient()
