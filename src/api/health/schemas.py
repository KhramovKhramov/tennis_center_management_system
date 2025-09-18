from pydantic import BaseModel, Field


class HealthResponseSchema(BaseModel):
    """Схема ответа на запрос о работоспособности системы."""

    status: str = Field(description='Статус')
