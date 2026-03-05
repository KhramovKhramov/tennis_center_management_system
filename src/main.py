"""Точка входа в приложение."""

from src.core.config import Settings
from src.entrypoints.api.registrar import create_app

settings = Settings()

app = create_app(settings)
