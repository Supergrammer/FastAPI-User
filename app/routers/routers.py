from fastapi import APIRouter

from .app_router import router as app_router
from .auth_router import router as auth_router
from .user_router import router as user_router
from .user_password_router import router as user_password_router

router = APIRouter()

user_router.include_router(user_password_router)

router.include_router(app_router)
router.include_router(auth_router)
router.include_router(user_router)
