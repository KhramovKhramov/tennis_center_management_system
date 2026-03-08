import asyncio
from collections.abc import Iterable

from src.application.use_cases.health.dto import HealthCheckResult
from src.domain.interfaces.health_checker import (
    ComponentHealthStatus,
    IComponentHealthChecker,
)


class HealthCheckUseCase:
    """Проверка работоспособности системы."""

    def __init__(self, checkers: Iterable[IComponentHealthChecker]):
        self._checkers = checkers

    async def execute(self) -> HealthCheckResult:
        check_tasks: list = [checker.check() for checker in self._checkers]
        if not check_tasks:
            return HealthCheckResult(is_healthy=True, components_statuses=[])
        results: list[ComponentHealthStatus] = await asyncio.gather(
            *check_tasks
        )

        is_system_healthy = all(result.is_healthy for result in results)

        return HealthCheckResult(
            is_healthy=is_system_healthy, components_statuses=results
        )
