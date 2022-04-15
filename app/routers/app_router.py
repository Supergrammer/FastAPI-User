from fastapi import APIRouter

from app.configurations.settings import get_settings

router = APIRouter(
    prefix="/app",
    tags=["app"],
)

@router.get("/info")
async def app_info():
    return get_settings()
