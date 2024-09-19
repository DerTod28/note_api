import collections
from typing import Any, Optional

from sqlalchemy import Row
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.models.api.v1.users import User
from app.schemas.users import UserCreate
from app.utils.password_hash import hash_password


class UserService:
    async def get_all_users(self, session: AsyncSession) -> collections.abc.Sequence[Row[Any]]:
        statement = select(User)
        result = await session.execute(statement)
        return result.all()

    async def get_user(self, username: str, session: AsyncSession) -> Optional[Any]:
        statement = select(User).where(User.username == username)
        result = await session.execute(statement)
        note = result.first()
        return note if note is not None else None

    async def username_exists(self, username: str, session: AsyncSession) -> Optional[bool]:
        statement = select(User).where(User.username == username)
        result = await session.execute(statement)
        user = result.first()
        return True if user else None

    async def create_user(self, user_data: UserCreate, session: AsyncSession) -> Any:
        hashed_password = hash_password(user_data.password)
        user_data.password = hashed_password
        user_data_dict = user_data.model_dump()

        new_user = User(**user_data_dict)
        session.add(new_user)
        await session.commit()
        return new_user
