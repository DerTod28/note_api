import uuid
from datetime import datetime

from pydantic import BaseModel


class Note(BaseModel):
    uid: uuid.UUID
    title: str
    content: str
    create_at: datetime
    updated_at: datetime
    to_user_uid: uuid.UUID


class NoteCreate(BaseModel):
    title: str
    content: str
