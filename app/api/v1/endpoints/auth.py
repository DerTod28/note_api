# from typing import Coroutine
#
# from fastapi import APIRouter, Depends
# from fastapi_jwt_auth import AuthJWT
# from sqlalchemy.ext.asyncio import AsyncSession
#
# from app.database import get_session
# from app.schemas.auth import Login
# from app.services.auth_service import AuthService
# from app.utils.exceptions import ApiExceptionsError
#
# router = APIRouter(
#     prefix='/auth',
#     tags=['auth'],
#     responses={
#         '404': ApiExceptionsError.not_found_404(as_dict=True)
#     }
# )
#
# auth_service = AuthService()
#
#
# @router.post('/login')
# async def login(login_data: Login, Authorize: AuthJWT, session: AsyncSession =
# Depends(get_session)) -> dict[str, str]:
#     if login_data.username != "test" or login_data.password != "test":
#         raise ApiExceptionsError.bad_request_400(detail="Bad username or password")
#     is_correct = auth_service.check_user_credentials(login_data, session)
#     if is_correct:
#         print(is_correct)
#     else:
#         print("NONONONOO")
#     # access_token = Authorize.create_access_token(subject=login_data.username)
#     # return {"access_token": access_token}
