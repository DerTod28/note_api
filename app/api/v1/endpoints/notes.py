import collections
import uuid

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.models.api.v1.notes import Note
from app.schemas.notes import NoteCreate
from app.services.notes_service import NoteService
from app.services.users_service import UserService
from app.utils.exceptions import ApiExceptionsError
from app.utils.yandex_speller import check_note_content_and_update

router = APIRouter(
    prefix='/notes',
    tags=['note'],
    responses={'404': ApiExceptionsError.not_found_404(as_dict=True)},  # type: ignore[dict-item]
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
note_service = NoteService()
user_service = UserService()


# /api/v1/notes/ - Получение всех заметок
@router.get('/', response_model=list[Note], description='Получение всех заметок')
async def get_all_notes(
    user_uid: uuid.UUID = Depends(user_service.get_current_user_uid),  # Get user UID from JWT
    session: AsyncSession = Depends(get_session),
) -> collections.abc.Sequence:  # type: ignore[type-arg]
    notes = await note_service.get_all_notes(user_uid, session)  # type: ignore[arg-type]
    return notes


# /api/v1/notes/<uuid:UUID>/ - Получение всех заметок
@router.get('/{note_uid}', response_model=Note, description='Получение одной заметки по UUID')
async def get_note(
    note_uid: str,
    user_uid: uuid.UUID = Depends(user_service.get_current_user_uid),  # Get user UID from JWT
    session: AsyncSession = Depends(get_session),
) -> collections.abc.Coroutine:  # type: ignore[type-arg]
    note = await note_service.get_note(note_uid, user_uid, session)  # type: ignore[arg-type]
    if not note:
        raise ApiExceptionsError.not_found_404(detail='Note not found')  # type: ignore[misc]
    return note


# /api/v1/notes/create/ - Создание новое заметок
@router.post('/create', response_model=Note, description='Создание одной новой заметки')
async def create_note(
    note_data: NoteCreate,
    user_uid: uuid.UUID = Depends(user_service.get_current_user_uid),  # Get user UID from JWT
    session: AsyncSession = Depends(get_session),
) -> collections.abc.Coroutine:  # type: ignore[type-arg]
    new_note = await note_service.create_note(note_data, user_uid, session)  # type: ignore[arg-type]
    check_note_content_and_update.delay(new_note.uid, note_data.content)
    return new_note
