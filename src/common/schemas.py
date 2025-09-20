from pydantic import BaseModel, Field


class ResponseIdMixinSchema(BaseModel):
    """Миксин, добавляющий поле id в Response-схемы."""

    id: int = Field(
        description='Идентификатор',
        examples=[1],
    )
