# from sqlmodel import select
# from sqlmodel.ext.asyncio.session import AsyncSession
# from app.schemas.auth import Login
# from app.models.api.v1.users import User
# from app.utils.password_hash import hash_password
#
#
# class AuthService:
#     async def check_user_credentials(self,  login_data: Login,  session: AsyncSession):
#         hashed_password = hash_password(login_data.password)
#         statement = select(User).where(
#             User.username == login_data.username, User.password == hashed_password,
#         )
#         result = await session.execute(statement)
#         user = result.first()
#         return True if user else False
