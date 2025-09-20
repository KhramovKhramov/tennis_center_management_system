from sqlalchemy.ext.asyncio import AsyncSession

from src.common.repository import SQLAlchemyRepository
from src.models import User


class UserRepository(SQLAlchemyRepository):
    """Класс-репозиторий для работы с моделью пользователя."""

    def __init__(self, session: AsyncSession, model: type[User]):
        super().__init__(session, model)
