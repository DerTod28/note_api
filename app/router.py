from fastapi import APIRouter

from app.api.v1.endpoints import auth, notes, users

api_router_v1 = APIRouter()

_v1_routers = [
    notes,
    users,
    auth,
]

for v1_route in _v1_routers:
    api_router_v1.include_router(
        v1_route.router,
        prefix='/api/v1',
    )
