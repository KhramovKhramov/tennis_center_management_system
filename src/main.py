"""Точка входа в приложение."""

from sqlalchemy.exc import NoResultFound

from src.common.exceptions import sqlalchemy_not_found_exception_handler
from src.core.registrar import register_app
from src.router import router

app = register_app()
app.include_router(router)

app.add_exception_handler(
    NoResultFound,
    sqlalchemy_not_found_exception_handler,
)
