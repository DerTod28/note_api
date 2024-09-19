# from sqlalchemy.orm import Mapped
#
# from app.database import BaseModel, int_pk, str_uniq
#
#
# class User(BaseModel):
#     """
#     class User:
#         id int
#         username: str
#         hashed_password: str
#     """
#     __tablename__ = "users"
#
#     id: Mapped[int_pk]  # noqa: VNE003
#     username: Mapped[str_uniq]
#     hashed_password: Mapped[str]
#
#     def __str__(self):
#         return f'{self.__class__.__name__}(id={self.id}, ' f'username={self.username!r},'
#
#     def __repr__(self):
#         return str(self)
#


# from sqlalchemy.orm import Mapped
#
# from app.database import BaseModel, int_pk, str_null_true
#
#
# class Note(BaseModel):
#     """
#     class Note:
#         id int
#         title: str
#         content: str
#         created_at: datetime
#     """
#     __tablename__ = "notes"
#
#     id: Mapped[int_pk]  # noqa: VNE003
#     title: Mapped[str]
#     content: Mapped[str_null_true]
#
#     # user: Mapped["User"] = relationship("User", back_populates="users")
#
#     def __str__(self):
#         return f'{self.__class__.__name__}(id={self.id}, ' f'title={self.title!r},'
#
# def __repr__(self):
#     return str(self)


import uuid
from datetime import datetime

import sqlalchemy.dialects.postgresql as pg
from sqlalchemy import Column
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __tablename__ = 'user'

    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4,
        ),
    )
    username: str
    password: str
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))

    def __repr__(self) -> str:
        return f'<User - {self.username}>'
