import collections

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.schemas.users import UserCreate
from app.services.users_service import UserService
from app.utils.exceptions import ApiExceptionsError

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


# /users/me
