"""Общие для приложения исключения."""

from fastapi import status
from fastapi.responses import JSONResponse


def sqlalchemy_not_found_exception_handler(*_):
    """
    Обработчик стандартного 404-случая, когда объект не найден в БД.
    """

    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            'detail': 'Объект с таким идентификатором не найден',
        },
    )
