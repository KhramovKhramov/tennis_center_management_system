import factory
from factory.alchemy import SQLAlchemyModelFactory

from src.models import User
from src.models.enums import GenderTypes
from tests.core.faker import faker


class UserFactory(SQLAlchemyModelFactory):
    """Фабрика данных пользователя."""

    last_name = factory.LazyFunction(lambda: faker.last_name_female())
    first_name = factory.LazyFunction(lambda: faker.first_name_female())
    patronymic = factory.LazyFunction(lambda: faker.middle_name_female())
    date_of_birth = factory.LazyFunction(
        lambda: faker.date_of_birth(minimum_age=18)
    )
    gender = GenderTypes.female
    email = factory.LazyAttribute(
        lambda obj: f'{obj.last_name.lower()}.'
        f'{obj.first_name.lower()}'
        f'{str(obj.date_of_birth)}@example.com'
    )
    phone_number = factory.LazyFunction(lambda: f'+79{faker.msisdn()[4:]}')

    class Meta:
        model = User
