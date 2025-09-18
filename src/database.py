"""Инициализация сессии для работы с базой данных."""

from collections.abc import AsyncGenerator

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.core.config import settings


def create_database_url() -> URL:
    """Формирование URL для подключения к БД."""

    return URL.create(
        drivername='postgresql+asyncpg',
        username=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        database=settings.DB_NAME,
    )


DATABASE_URL = create_database_url()

engine = create_async_engine(DATABASE_URL, echo=settings.DEBUG)
async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Генератор, возвращающий асинхронную сессию подключения к БД.
    """

    async with async_session() as session:
        try:
            yield session
        except Exception as exc:
            await session.rollback()
            raise exc
        else:
            await session.commit()
