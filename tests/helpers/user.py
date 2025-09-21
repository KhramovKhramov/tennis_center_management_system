from src.models import User
from tests.factories.user import UserFactory


async def create_user_request_data() -> dict:
    """
    Получение словаря с данными, необходимыми для
    создания пользователя.
    """

    instance = UserFactory.build()

    return {
        'first_name': instance.first_name,
        'last_name': instance.last_name,
        'patronymic': instance.patronymic,
        'date_of_birth': str(instance.date_of_birth),
        'gender': instance.gender,
        'email': instance.email,
        'phone_number': instance.phone_number,
    }


async def update_user_request_data() -> dict:
    """
    Получение словаря с данными, необходимыми для
    обновления пользователя.
    """

    return await create_user_request_data()


async def serialize_user(user: User) -> dict:
    """Сериализация модели пользователя для использования в тестах."""

    return {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'patronymic': user.patronymic,
        'date_of_birth': user.date_of_birth.strftime('%Y-%m-%d'),
        'gender': user.gender,
        'email': user.email,
        'phone_number': user.phone_number,
        'is_active': user.is_active,
        'join_time': user.join_time.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
    }
