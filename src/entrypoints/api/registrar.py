from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from src.core.config import Settings
from src.entrypoints.api.openapi import TAGS_METADATA
from src.entrypoints.api.router import api_router
from src.infra.di.settings import SettingsProvider
from src.infra.di.use_cases import UseCaseProvider


def create_app(settings: Settings) -> FastAPI:
    """Регистрация FastAPI-приложения."""

    app = FastAPI(
        title=settings.FASTAPI_TITLE,
        version=settings.FASTAPI_VERSION,
        description=settings.FASTAPI_DESCRIPTION,
        docs_url=settings.FASTAPI_DOCS_URL,
        redoc_url=settings.FASTAPI_REDOC_URL,
        openapi_url=settings.FASTAPI_OPENAPI_URL,
        openapi_tags=TAGS_METADATA,
    )

    # Подключение API-роутеров
    app.include_router(api_router)

    # Подключение DI
    container = make_async_container(
        SettingsProvider(settings=settings),
        UseCaseProvider(),
    )
    setup_dishka(container, app)

    return app
