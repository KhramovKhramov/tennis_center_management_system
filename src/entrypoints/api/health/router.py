from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, status

from src.application.use_cases.health.health_check import HealthCheckUseCase
from src.entrypoints.api.health.schemas import HealthCheckResponse

router = APIRouter(prefix="/health", tags=["health"])


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="Проверка работоспособности системы",
    response_model=HealthCheckResponse,
)
@inject
async def health_check(use_case: FromDishka[HealthCheckUseCase]):
    result = await use_case.execute()
    return HealthCheckResponse(is_healthy=result.is_healhty)
