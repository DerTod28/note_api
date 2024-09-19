import uuid
from typing import Any

from sqlmodel import desc, select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.models.api.v1.notes import Note
from app.schemas.notes import NoteCreate


class NoteService:
    async def get_all_notes(self, session: AsyncSession) -> Any:
        statement = select(Note).order_by(desc(Note.created_at))  # TODO filter by user
        result = await session.execute(statement)
        return result.all()

    async def get_note(self, note_uid: uuid.UUID, session: AsyncSession) -> Any:
        statement = select(Note).where(Note.uid == note_uid)
        result = await session.execute(statement)
        note = result.first()
        return note if note is not None else None

    async def create_note(self, note_data: NoteCreate, session: AsyncSession) -> Any:
        note_data_dict = note_data.model_dump()
        new_note = Note(**note_data_dict)
        session.add(new_note)
        await session.commit()
        return new_note
