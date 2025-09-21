from src.api.v1.user.schemas import (
    UserCreateSchema,
    UserResponseSchema,
    UserUpdateSchema,
)
from src.common.repository import SQLAlchemyRepository


class UserService:
    """Сервис пользователей."""

    def __init__(self, repository: SQLAlchemyRepository):
        self._repository: SQLAlchemyRepository = repository

    async def create_user(self, data: UserCreateSchema) -> UserResponseSchema:
        """Создание пользователя."""

        return UserResponseSchema.model_validate(
            await self._repository.insert_one(
                data.model_dump(exclude_unset=True)
            )
        )

    async def get_user_by_id(self, user_id: int) -> UserResponseSchema:
        """Получение пользователя по идентификатору."""

        return UserResponseSchema.model_validate(
            await self._repository.select_one(user_id)
        )

    async def get_users(self) -> list[UserResponseSchema]:
        """Получение списка пользователей."""

        return [
            UserResponseSchema.model_validate(user)
            for user in await self._repository.select_many()
        ]

    async def update_user(
        self, user_id: int, data: UserUpdateSchema
    ) -> UserResponseSchema:
        """Обновление данных пользователя."""

        return UserResponseSchema.model_validate(
            await self._repository.update_one(
                user_id, data.model_dump(exclude_unset=True)
            )
        )

    async def delete_user(self, user_id: int) -> None:
        """Удаление пользователя."""

        await self._repository.delete_one(user_id)
