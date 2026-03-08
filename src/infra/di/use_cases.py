from dishka import Provider, Scope, provide

from src.application.use_cases.health.health_check import HealthCheckUseCase


class UseCaseProvider(Provider):
    """Провайдер юзкейсов приложения."""

    scope = Scope.REQUEST

    @provide
    def get_health_use_case(self) -> HealthCheckUseCase:
        return HealthCheckUseCase()
