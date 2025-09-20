from datetime import date, datetime

import phonenumbers
from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    field_validator,
)

from src.common.schemas import ResponseIdMixinSchema
from src.models.enums import GenderTypes


class UserBaseSchema(BaseModel):
    """Базовая схема данных пользователя."""

    last_name: str = Field(description='Фамилия', max_length=50)
    first_name: str = Field(description='Имя', max_length=50)
    patronymic: str | None = Field(
        description='Отчество', default=None, max_length=50
    )
    date_of_birth: date = Field(description='Дата рождения')
    gender: GenderTypes = Field(description='Пол')
    email: EmailStr = Field(description='Email', max_length=50)
    phone_number: str = Field(description='Номер телефона')

    @field_validator('phone_number')
    def validate_phone_number(cls, v):
        """Валидация номера телефона."""

        try:
            parsed = phonenumbers.parse(v, 'RU')
            if not phonenumbers.is_valid_number(parsed):
                raise ValueError('Неверный номер телефона')
            # Приводим к международному формату без разделителей
            return phonenumbers.format_number(
                parsed, phonenumbers.PhoneNumberFormat.E164
            )
        except phonenumbers.NumberParseException as err:
            raise ValueError('Неверный формат номера телефона') from err


class UserCreateSchema(UserBaseSchema):
    """Схема создания пользователя."""


class UserUpdateSchema(UserBaseSchema):
    """Схема обновления пользователя."""

    last_name: str | None = Field(
        description='Фамилия', default=None, max_length=50
    )
    first_name: str | None = Field(
        description='Имя', default=None, max_length=50
    )
    patronymic: str | None = Field(
        description='Отчество', default=None, max_length=50
    )
    date_of_birth: date | None = Field(
        description='Дата рождения', default=None
    )
    gender: GenderTypes | None = Field(description='Пол', default=None)
    email: EmailStr | None = Field(
        description='Email', default=None, max_length=50
    )
    phone_number: str | None = Field(
        description='Номер телефона', default=None
    )


class UserResponseSchema(UserBaseSchema, ResponseIdMixinSchema):
    """Схема ответа API пользователя."""

    is_active: bool = Field(description='Активен', examples=[True, False])
    join_time: datetime = Field(description='Дата регистрации')

    model_config = ConfigDict(from_attributes=True)
