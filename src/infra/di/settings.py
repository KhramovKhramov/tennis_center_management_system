from dishka import Provider, Scope, provide

from src.core.config import Settings


class SettingsProvider(Provider):
    """Провайдер настроек приложения."""

    def __init__(self, settings: Settings) -> None:
        super().__init__()
        self._settings = settings

    @provide(scope=Scope.APP)
    def get_settings(self) -> Settings:
        return self._settings
