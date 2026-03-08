from dataclasses import dataclass
from typing import Protocol


@dataclass
class ComponentHealthStatus:
    component_name: str
    is_healthy: bool
    error_msg: str | None = None


class IComponentHealthChecker(Protocol):
    async def check(self) -> ComponentHealthStatus:
        """Проверяет конкретный компонент и возвращает его статус."""
        ...
