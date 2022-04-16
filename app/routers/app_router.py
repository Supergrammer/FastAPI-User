from fastapi import APIRouter

from app.configurations.settings import get_settings

router = APIRouter(
    prefix="/app",
    tags=["app"],
)


@router.get("/info")
async def app_info():
    return get_settings()


@router.get("/health-check")
async def health_check():
    return {"healthy": True}
