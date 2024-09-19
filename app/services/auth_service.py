from typing import Any

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.models.api.v1.users import User
from app.schemas.auth import Login
from app.utils.password_hash import hash_password, verify_password


class AuthService:
    async def get_user_by_credentials(self, login_data: Login, session: AsyncSession) -> Any:
        user = None
        hashed_password = hash_password(login_data.password)
        if verify_password(login_data.password, hashed_password):
            statement = select(User).where(
                User.username == login_data.username,
            )
            result = await session.execute(statement)
            user = result.scalars().first()
        return user if user else False
