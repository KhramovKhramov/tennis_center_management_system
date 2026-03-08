from pydantic import BaseModel, Field


class HealthCheckResponse(BaseModel):
    """Схема ответа на запрос о работоспособности системы."""

    is_healthy: bool = Field(description="Статус")
