from abc import ABC, abstractmethod

from django.db.models import Case, CharField, F, Q, Value, When
from django.db.models.functions import Concat


class UserFullNameAnnotationMixin(ABC):
    """
    Абстрактный класс, добавляющий возможность с помощью метода
    with_full_name_annotation добавить к кверисету аннотированную строку с
    полным именем пользователя.

    Для корректной работы необходимо добавить к классу-наследнику аттрибут
    user_field_name с путем до поля user.
    """

    @property
    @abstractmethod
    def user_field_name(self):
        raise NotImplementedError()

    def with_full_name_annotation(self):
        """Добавляет к кверисету аннотацию с ФИО пользователя."""

        field_name = self.user_field_name
        user_lookup = '' if not field_name else f'{field_name}__'

        return self.annotate(
            full_name=Concat(
                F(f'{user_lookup}last_name'),
                Value(' '),
                F(f'{user_lookup}first_name'),
                Case(
                    When(
                        Q(**{f'{user_lookup}patronymic__isnull': True})
                        | Q(**{f'{user_lookup}patronymic': ''}),
                        then=Value(''),
                    ),
                    default=Concat(
                        Value(' '),
                        F(f'{user_lookup}patronymic'),
                    ),
                ),
                output_field=CharField(),
            )
        )
