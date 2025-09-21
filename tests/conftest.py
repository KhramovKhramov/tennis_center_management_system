"""Общие фикстуры для тестов."""

import asyncpg
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.common.models import Base
from src.database import get_session
from src.main import app
from tests.core.config import test_settings

# PostgreSQL


@pytest_asyncio.fixture(scope='session')
async def create_test_db():
    """Фикстура для создания тестовой БД на время сессии выполнения тестов."""

    # Подключаемся к системной БД
    sys_conn = await asyncpg.connect(
        user=test_settings.TEST_DB_USER,
        password=test_settings.TEST_DB_PASSWORD,
        host=test_settings.TEST_DB_HOST,
        port=test_settings.TEST_DB_PORT,
    )

    # Создаем тестовую БД, если ее не существует
    try:
        await sys_conn.execute(f'CREATE DATABASE {test_settings.TEST_DB_NAME}')
    except asyncpg.exceptions.DuplicateDatabaseError:
        pass
    finally:
        await sys_conn.close()


@pytest_asyncio.fixture(scope='function')
async def test_engine(create_test_db):
    """Фикстура с engine для подключения к БД."""

    engine = create_async_engine(test_settings.test_database_url)
    yield engine
    await engine.dispose()


@pytest_asyncio.fixture(scope='function')
async def test_session(test_engine):
    """
    Фикстура, создающая новую асинхронную сессию
    БД с автоматическим откатом изменений после теста.
    """

    test_async_session = async_sessionmaker(
        test_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    async with test_engine.begin() as conn:
        # Создаем все таблицы перед тестом
        await conn.run_sync(Base.metadata.create_all)

    async with test_async_session() as session:
        yield session

    # Удаляем все таблицы после теста
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture(scope='function')
async def unauthorized_client(test_session):
    """
    Фикстура, возвращающая тестовый клиент для отправки запросов
    и тестирования API.
    """

    # Подменяем зависимость, возвращающую сессию (то есть во время тестов app
    # будет использовать зависимость с подключением к тестовой БД,
    # а не основной)
    async def override_get_session():
        yield test_session

    app.dependency_overrides[get_session] = override_get_session

    async with AsyncClient(
        transport=ASGITransport(app),
        base_url='https://test',
    ) as client:
        yield client


@pytest_asyncio.fixture(scope='session', autouse=True)
async def drop_test_db():
    """
    Фикстура удаления тестовой БД после выполнения всех тестов.
    """

    yield  # Ждем окончания всех тестов

    # Подключаемся к системной БД для удаления тестовой
    sys_conn = await asyncpg.connect(
        user=test_settings.TEST_DB_USER,
        password=test_settings.TEST_DB_PASSWORD,
        host=test_settings.TEST_DB_HOST,
        port=test_settings.TEST_DB_PORT,
    )
    try:
        await sys_conn.execute(
            f'DROP DATABASE {test_settings.TEST_DB_NAME} WITH (FORCE)'
        )
    except asyncpg.exceptions.PostgresError as e:
        raise e
    finally:
        await sys_conn.close()
