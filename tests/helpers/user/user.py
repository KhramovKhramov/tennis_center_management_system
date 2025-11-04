from datetime import date

from apps.user.models import User

from tests.factories import UserFactory


def get_create_user_request_data_only_required_fields() -> dict:
    """
    Получение словаря с данными, необходимыми для
    создания пользователя только с обязательными полями.
    """

    instance = UserFactory.build()

    return {
        'last_name': instance.last_name,
        'first_name': instance.first_name,
        'username': instance.username,
        'date_of_birth': instance.date_of_birth,
        'gender': instance.gender,
        'email': instance.email,
        'phone_number': instance.phone_number,
        'password': 'qwerty',
    }


def get_create_user_request_data_all_fields() -> dict:
    """
    Получение словаря с данными, необходимыми для
    создания пользователя со всеми полями.
    """

    data = get_create_user_request_data_only_required_fields()
    data.update(
        {
            'patronymic': 'Отчество',
        }
    )

    return data


def get_update_user_request_data() -> dict:
    """
    Получение словаря с данными, необходимыми для
    обновления данных пользователя.
    """

    instance = UserFactory.build()
    update_fields = ['first_name', 'last_name', 'patronymic', 'date_of_birth']

    return {key: getattr(instance, key) for key in update_fields}


def serialize_user(user: User) -> dict:
    """Сериализация объекта модели пользователя в тестах."""

    return {
        'id': user.pk,
        'last_name': user.last_name,
        'first_name': user.first_name,
        'patronymic': user.patronymic,
        'username': user.username,
        'date_of_birth': user.date_of_birth.strftime('%Y-%m-%d')
        if isinstance(user.date_of_birth, date)
        else user.date_of_birth,
        'gender': user.gender,
        'email': user.email,
        'phone_number': user.phone_number,
    }
