from collections.abc import Iterable

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.interfaces.health_checker import IComponentHealthChecker
from src.infra.health_checkers import PostgresHealthChecker


class HealthCheckersProvider(Provider):
    """Провайдер проверок работоспобности системы."""

    scope = Scope.REQUEST

    @provide
    def get_pg_checker(self, session: AsyncSession) -> PostgresHealthChecker:
        return PostgresHealthChecker(session)

    @provide
    def get_all_checkers(
        self,
        pg_checker: PostgresHealthChecker,
    ) -> Iterable[IComponentHealthChecker]:
        return [pg_checker]
