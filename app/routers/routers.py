from fastapi import APIRouter

from .user_account_router import router as user_account_router

router = APIRouter()

router.include_router(user_account_router)