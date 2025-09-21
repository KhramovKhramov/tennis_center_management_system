async def serialize_healthcheck() -> dict:
    """Сериализация ответа healthcheck-эндпоинта."""

    return {
        'status': 'ok',
    }
