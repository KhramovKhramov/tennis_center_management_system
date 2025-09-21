import pytest
from fastapi import status

from tests.core.urls_config import HEALTH_API_URL
from tests.helpers.health import serialize_healthcheck


@pytest.mark.asyncio
async def test_health_check(unauthorized_client):
    """
    Тест эндпоинта работоспособности системы.

    Ожидание: статус 200 в ответе ожидаемого формата.
    """

    response = await unauthorized_client.get(HEALTH_API_URL)
    assert response.status_code == status.HTTP_200_OK
    response_data = response.json()

    assert response_data == await serialize_healthcheck()
