import uuid
from typing import Any, Coroutine, Optional, Sequence

from sqlmodel import desc, select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.models.api.v1.notes import Note
from app.schemas.notes import NoteCreate


class NoteService:
    async def get_all_notes(self, user_uid: uuid.UUID, session: AsyncSession) -> Sequence[Note]:
        statement = select(Note).where(Note.to_user_uid == user_uid).order_by(desc(Note.created_at))
        result = await session.execute(statement)
        return result.scalars().all()

    async def get_note(
        self,
        note_uid: uuid.UUID,
        user_uid: uuid.UUID,
        session: AsyncSession,
    ) -> Optional[Coroutine[Any, Any, Any]]:
        statement = select(Note).where(Note.uid == note_uid, Note.to_user_uid == user_uid)
        result = await session.execute(statement)
        note = result.scalars().first()
        return note if note is not None else None

    async def create_note(self, note_data: NoteCreate, user_uid: uuid.UUID, session: AsyncSession) -> Any:
        note_data_dict = note_data.model_dump()
        new_note = Note(**note_data_dict)
        new_note.to_user_uid = user_uid
        session.add(new_note)
        await session.commit()
        return new_note
