from dataclasses import dataclass

from src.domain.interfaces.health_checker import (
    ComponentHealthStatus,
)


@dataclass
class HealthCheckResult:
    is_healthy: bool
    components_statuses: list[ComponentHealthStatus]
