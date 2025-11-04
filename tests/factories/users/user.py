import factory
from apps.users.models import User
from apps.users.models.choices import GenderType


class UserFactory(factory.django.DjangoModelFactory):
    """Фабрика данных пользователя."""

    last_name = factory.Faker('last_name_female', locale='ru_RU')
    first_name = factory.Faker('first_name_female', locale='ru_RU')
    patronymic = factory.Faker('middle_name', locale='ru_RU')
    username = factory.Sequence(lambda n: f'user_{n}')
    date_of_birth = factory.Faker('date_of_birth', minimum_age=18)
    gender = GenderType.FEMALE
    email = factory.Sequence(lambda n: f'user{n}@example.com')
    phone_number = factory.Faker('numerify', text='+7(9##)###-####')

    class Meta:
        model = User
