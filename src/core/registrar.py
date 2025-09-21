"""Регистрация FastAPI-приложения и его компонентов."""

from fastapi import APIRouter, FastAPI
from sqlalchemy.exc import NoResultFound

from src.api.v1.health.router import router as health_router
from src.api.v1.user.router import router as user_router
from src.common.exceptions import sqlalchemy_not_found_exception_handler
from src.core.config import settings
from src.core.swagger_config import TAGS_METADATA


def register_app() -> FastAPI:
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

    register_routers(app)
    register_exceptions(app)

    return app


def register_routers(app: FastAPI) -> None:
    """Регистрация API-роутеров приложения."""

    main_router = APIRouter(prefix='/api')
    v1_router = APIRouter(prefix='/v1')

    v1_routers = (
        health_router,
        user_router,
    )
    for router in v1_routers:
        v1_router.include_router(router)

    main_router.include_router(v1_router)

    app.include_router(main_router)


def register_exceptions(app: FastAPI) -> None:
    """Регистрация исключений."""

    app.add_exception_handler(
        NoResultFound,
        sqlalchemy_not_found_exception_handler,
    )
