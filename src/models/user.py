from datetime import date, datetime

from sqlalchemy import Boolean, Date, DateTime, Enum, String, false, true
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.functions import now

from src import models
from src.common.models import Base
from src.models.enums import GenderTypes


class User(Base):
    """Модель пользователя системы."""

    __tablename__ = 'users'

    # Данные пользователя
    last_name: Mapped[str] = mapped_column(
        String(50), index=True, comment='Фамилия'
    )
    first_name: Mapped[str] = mapped_column(
        String(50), index=True, comment='Имя'
    )
    patronymic: Mapped[str | None] = mapped_column(
        String(50), index=True, comment='Отчество'
    )
    date_of_birth: Mapped[date] = mapped_column(
        Date(), comment='Дата рождения'
    )
    gender: Mapped[GenderTypes] = mapped_column(
        Enum(GenderTypes), comment='Пол'
    )

    # Контактная информация
    email: Mapped[str] = mapped_column(
        String(50), unique=True, index=True, comment='Email'
    )
    phone_number: Mapped[str] = mapped_column(
        String(12), unique=True, index=True, comment='Номер телефона'
    )

    # Техническая информация
    is_superuser: Mapped[bool] = mapped_column(
        Boolean(), server_default=false(), comment='Суперюзер'
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean(), server_default=true(), comment='Активен'
    )
    join_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=now(),
        comment='Дата регистрации',
    )

    # Роли
    administrator: Mapped['models.administrator.Administrator'] = relationship(
        back_populates='user', uselist=False
    )
