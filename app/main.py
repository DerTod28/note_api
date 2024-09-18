from fastapi import FastAPI

from app.router import api_router_v1

app = FastAPI(
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    redoc_url='/api/redoc',
)

app.include_router(api_router_v1)
