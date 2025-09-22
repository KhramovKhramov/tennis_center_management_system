from datetime import date

from sqlalchemy import Date, MetaData
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(AsyncAttrs, DeclarativeBase):
    """Базовая модель SQLAlchemy для наследования моделей базы данных."""

    id: Mapped[int] = mapped_column(
        'id',
        primary_key=True,
        autoincrement=True,
        comment='Идентификатор',
    )

    metadata = MetaData(
        naming_convention={
            'ix': 'ix_%(column_0_label)s',
            'uq': 'uq_%(table_name)s_%(column_0_name)s',
            'ck': 'ck_%(table_name)s_`%(constraint_name)s`',
            'fk': (
                'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s'
            ),
            'pk': 'pk_%(table_name)s',
        },
    )

    def __repr__(self):
        """Печать ORM-объектов с отображением атрибутов."""

        fmt = '{}.{}({})'
        package = self.__class__.__module__
        class_ = self.__class__.__name__
        attrs = sorted(
            (k, getattr(self, k)) for k in self.__mapper__.columns.keys()
        )
        sattrs = ', '.join('{}={!r}'.format(*x) for x in attrs)

        return fmt.format(package, class_, sattrs)


class DatesRangeMixin:
    """
    Миксин, добавляет к моделям ролей поля с датами
    начала и окончания действия роли.
    """

    date_from: Mapped[date] = mapped_column(
        Date(), comment='Дата начала действия роли'
    )
    date_to: Mapped[date | None] = mapped_column(
        Date(), comment='Дата окончания действия роли'
    )
