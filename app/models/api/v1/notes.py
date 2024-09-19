import uuid
from datetime import datetime

import sqlalchemy.dialects.postgresql as pg
from sqlalchemy import Column, ForeignKey
from sqlmodel import Field, SQLModel


class Note(SQLModel, table=True):
    __tablename__ = 'note'

    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4,
        ),
    )
    title: str
    content: str
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    to_user_uid: uuid.UUID = Field(sa_column=Column(pg.UUID, ForeignKey('user.uid'), nullable=False))

    def __repr__(self) -> str:
        return f'<Note - {self.title}>'
