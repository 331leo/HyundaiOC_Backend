from fastapi import APIRouter

from .login import login_router
from .users import users_router
# from .users import users_router

v1_router = APIRouter()

# v1_router.include_router(users_router, prefix="/users", tags=["users"])
v1_router.include_router(login_router, prefix="/login", tags=["login"])
v1_router.include_router(users_router, prefix="/users", tags=["users"])