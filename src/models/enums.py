"""Файл enums для использования в моделях БД."""

from enum import StrEnum, auto


class GenderTypes(StrEnum):
    """Пол."""

    male = auto()
    female = auto()
