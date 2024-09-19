from celery import Celery

from app.core.config import get_redis_url

app = Celery(
    'notes-tasks',
    broker=get_redis_url(),
    backend=get_redis_url(),
)

app.autodiscover_tasks(['app.utils.yandex_speller'])
