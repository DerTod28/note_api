from fastapi import FastAPI

from app.database import init_db
from app.router import api_router_v1

app = FastAPI(
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    redoc_url='/api/redoc',
)

app.include_router(api_router_v1)


@app.on_event('startup')
async def startup_event() -> None:
    await init_db()
