import collections
import uuid

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import Row
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.models.api.v1.users import User
from app.schemas.users import CurrentUser, UserCreate
from app.services.users_service import UserService
from app.utils.exceptions import ApiExceptionsError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

router = APIRouter(
    prefix='/users',
    tags=['user'],
    responses={'404': ApiExceptionsError.not_found_404(as_dict=True)},  # type: ignore[dict-item]
)
user_service = UserService()


# /api/v1/users/create/ - Создание нового пользователя
@router.post('/create', response_model=UserCreate, description='Создание нового пользователя')
async def create_user(
    user: UserCreate,
    session: AsyncSession = Depends(get_session),
) -> collections.abc.Coroutine:  # type: ignore[type-arg]
    user_exists = await user_service.username_exists(user.username, session)  # type: ignore[arg-type]
    if user_exists:
        raise ApiExceptionsError.bad_request_400(detail='Username is already taken')  # type: ignore[misc]
    new_user = await user_service.create_user(user, session)  # type: ignore[arg-type]
    return new_user


# /users/me - Текущий пользователь
@router.get('/me', response_model=CurrentUser, description='Текущий пользователь - JWT TOKEN из /login')
async def read_users_me(
    token: str = Depends(oauth2_scheme),
    current_user_uid: uuid.UUID = Depends(user_service.get_current_user_uid),
    session: AsyncSession = Depends(get_session),
) -> Row[tuple[User, ...]]:
    """
    Get current user details
    """
    cur_user = await user_service.get_user_by_uid(current_user_uid, session)  # type: ignore[arg-type]
    return cur_user
