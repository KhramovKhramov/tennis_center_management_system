from faker import Faker
from faker_enum import EnumProvider

faker = Faker('ru_RU')
faker.add_provider(EnumProvider)
