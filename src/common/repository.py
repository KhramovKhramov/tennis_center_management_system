"""Базовые реализация репозитория."""

from collections.abc import Sequence

from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.common.models import Base


class SQLAlchemyRepository:
    """Класс-репозиторий для работы с базой данных через SQLAlchemy."""

    def __init__(self, session: AsyncSession, model: type[Base]):
        self._session = session
        self._model = model

    async def insert_one(self, data: dict) -> Base:
        stmt = insert(self._model).values(**data).returning(self._model)
        result = await self._session.execute(stmt)

        return result.scalar_one()

    async def select_one(self, obj_id: int) -> Base:
        query = select(self._model).filter_by(id=obj_id)
        result = await self._session.execute(query)

        return result.scalar_one()

    async def select_many(self) -> Sequence[Base]:
        query = select(self._model)
        result = await self._session.execute(query)

        return result.scalars().all()

    async def update_one(self, obj_id: int, data: dict) -> Base:
        stmt = (
            update(self._model)
            .filter_by(id=obj_id)
            .values(**data)
            .returning(self._model)
        )
        result = await self._session.execute(stmt)

        return result.scalar_one()

    async def delete_one(self, obj_id: int) -> None:
        stmt = delete(self._model).filter_by(id=obj_id)
        await self._session.execute(stmt)
