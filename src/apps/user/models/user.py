from apps.user.models.choices import GenderType
from apps.user.models.managers import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.functional import cached_property


class User(AbstractBaseUser, PermissionsMixin):
    """Модель пользователя системы."""

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'date_of_birth',
        'email',
        'phone_number',
    ]

    # Данные пользователя
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=50,
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=50,
    )
    patronymic = models.CharField(
        verbose_name='Отчество',
        max_length=50,
        null=True,
        blank=True,
    )
    username = models.CharField(
        verbose_name='Логин',
        max_length=50,
        unique=True,
    )
    date_of_birth = models.DateField(
        verbose_name='Дата рождения',
    )
    gender = models.CharField(
        verbose_name='Пол',
        choices=GenderType.choices,
    )

    # Контактная информация
    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        unique=True,
    )
    phone_number = models.CharField(
        verbose_name='Номер телефона',
        unique=True,
        # TODO добавить валидацию номера телефона,
    )

    # Техническая информация
    created_at = models.DateTimeField(
        verbose_name='Дата и время регистрации',
        auto_now_add=True,
    )
    is_active = models.BooleanField(verbose_name='Активен', default=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return self.full_name

    @cached_property
    def full_name(self) -> str:
        """Возвращает ФИО пользователя."""

        full_name = (
            f'{self.last_name} {self.first_name} {self.patronymic or ""}'
        )

        return full_name.strip()

    @property
    def is_staff(self) -> bool:
        """Свойство для панели администратора."""

        return self.is_superuser
