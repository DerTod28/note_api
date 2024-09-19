import uuid
from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    uid: uuid.UUID
    username: str
    password: str
    create_at: datetime
    updated_at: datetime


class UserCreate(BaseModel):
    username: str
    password: str
