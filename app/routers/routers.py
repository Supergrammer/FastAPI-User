from fastapi import APIRouter

from .app_router import router as app_router

from .user_account_router import router as user_account_router
from .user_auth_router import router as user_auth_router

router = APIRouter()

router.include_router(app_router)
router.include_router(user_account_router)
router.include_router(user_auth_router)