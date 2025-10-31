from common.mixins import UserFullNameAnnotationMixin
from django.contrib.auth.base_user import BaseUserManager
from django.db.models import QuerySet


class UserQuerySet(QuerySet, UserFullNameAnnotationMixin):
    user_field_name = None


class UserManager(BaseUserManager):
    """Менеджер для модели пользователя."""

    use_in_migrations = True

    def get_queryset(self):
        return UserQuerySet(
            model=self.model,
            using=self._db,
            hints=self._hints,
        )

    def create_user(self, username, password=None, **kwargs):
        """Создание учетной записи пользователя."""

        if username is None:
            raise TypeError('У пользователя должен быть указан логин.')

        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password, **kwargs):
        """Создание учетной записи суперюзера."""

        kwargs.setdefault('is_superuser', True)

        if password is None:
            raise TypeError('У суперюзера должен быть пароль.')

        return self.create_user(username, password, **kwargs)
