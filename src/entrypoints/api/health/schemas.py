from pydantic import BaseModel, Field


class HealthCheckResponse(BaseModel):
    """Схема ответа на запрос о работоспособности системы."""

    status: str = Field(description="Статус")
