from sqlalchemy.orm import Mapped

from app.database import BaseModel, int_pk, str_null_true


class Note(BaseModel):
    """
    class Note:
        id int
        title: str
        content: str
        created_at: datetime
    """

    id: Mapped[int_pk]  # noqa: VNE003
    title: Mapped[str]
    content: Mapped[str_null_true]

    # user: Mapped["User"] = relationship("User", back_populates="users")

    def __str__(self):
        return f'{self.__class__.__name__}(id={self.id}, ' f'title={self.title!r},'

    def __repr__(self):
        return str(self)
