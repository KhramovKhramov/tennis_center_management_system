from dataclasses import dataclass


@dataclass
class HealthCheckResult:
    is_healhty: bool


class HealthCheckUseCase:
    """Проверка работоспособности системы."""

    async def execute(self) -> HealthCheckResult:
        return HealthCheckResult(is_healhty=True)
