from fastapi import APIRouter, status

from src.entrypoints.api.health.schemas import HealthCheckResponse

router = APIRouter(prefix="/health", tags=["health"])


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="Проверка работоспособности системы",
    response_model=HealthCheckResponse,
)
async def health_check():
    return {"status": "ok"}
