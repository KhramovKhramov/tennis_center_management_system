"""Регистрация FastAPI-приложения и его компонентов."""

from fastapi import FastAPI

from src.core.config import settings
from src.core.swagger_config import TAGS_METADATA


def register_app() -> FastAPI:
    """Регистрация FastAPI-приложения."""

    return FastAPI(
        title=settings.FASTAPI_TITLE,
        version=settings.FASTAPI_VERSION,
        description=settings.FASTAPI_DESCRIPTION,
        docs_url=settings.FASTAPI_DOCS_URL,
        redoc_url=settings.FASTAPI_REDOC_URL,
        openapi_url=settings.FASTAPI_OPENAPI_URL,
        openapi_tags=TAGS_METADATA,
    )
