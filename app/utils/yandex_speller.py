import asyncio
import logging
from typing import Any

import requests
from celery import shared_task
from sqlalchemy import update

from app.database import get_session
from app.models.api.v1.notes import Note

YANDEX_SPELLER_API_URL = 'https://speller.yandex.net/services/spellservice.json/checkText'


@shared_task
def check_note_content_and_update(note_uid: str, content: str) -> None:
    """
    Celery task to check note content using Yandex Speller and update it in the DB.
    """
    # Since this task is synchronous, we need to run async functions using asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_check_and_update_content(note_uid, content))


async def _check_and_update_content(note_uid: str, content: str) -> None:
    """
    Asynchronously checks and updates the note content.
    """
    params = {'text': content, 'lang': 'ru', 'format': 'plain'}

    try:
        response = requests.get(YANDEX_SPELLER_API_URL, params=params)
        response.raise_for_status()
        corrections = response.json()

        if corrections:
            corrected_content = await apply_corrections(content, corrections)
            await save_corrected_content_to_db(note_uid, corrected_content)

    except requests.exceptions.RequestException as e:
        logging.info(f'Error checking content for note {note_uid}: {e}')


async def apply_corrections(content: str, corrections: Any) -> str:
    """
    Apply corrections returned by Yandex Speller.
    """
    for correction in corrections:
        content = content.replace(correction['word'], correction['s'][0])
    return content


async def save_corrected_content_to_db(note_uid: str, corrected_content: str) -> None:
    async for session in get_session():  # type: ignore[attr-defined]
        async with session.begin():
            statement = (
                update(Note).where(Note.uid == note_uid).values(content=corrected_content)  # type: ignore[arg-type]
            )
            await session.execute(statement)
            await session.commit()
