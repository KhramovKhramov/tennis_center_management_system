from fastapi import APIRouter, status
from sqlalchemy import text

from src.api.health.schemas import HealthResponseSchema
from src.common.dependencies import SessionDep

router = APIRouter(prefix='/health', tags=['health'])


@router.get(
    '/',
    status_code=status.HTTP_200_OK,
    summary='Проверка работоспособности системы',
    response_model=HealthResponseSchema,
)
async def health(session: SessionDep):
    # Проверка доступности PostgreSQL
    await session.execute(text('SELECT 1'))

    return {'status': 'ok'}
