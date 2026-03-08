from pydantic import BaseModel, ConfigDict, Field


class ComponentStatus(BaseModel):
    """Статус работоспособности компонента системы."""

    component_name: str = Field(description="Наименование компонента")
    is_healthy: bool = Field(description="Статус работоспосбности компомнента")
    error_msg: str | None = Field(default=None, description="Описание ошибки")


class HealthCheckResponse(BaseModel):
    """Схема ответа на запрос о работоспособности системы."""

    is_healthy: bool = Field(description="Статус")
    components_statuses: list[ComponentStatus]

    model_config = ConfigDict(from_attributes=True)
