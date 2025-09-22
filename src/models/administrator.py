from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src import models
from src.common.models import Base, DatesRangeMixin


class Administrator(Base, DatesRangeMixin):
    """Модель администратора."""

    __tablename__ = 'administrators'

    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete='RESTRICT'),
        unique=True,
        index=True,
        comment='Пользователь',
    )
    user: Mapped['models.user.User'] = relationship(
        back_populates='administrator',
    )
