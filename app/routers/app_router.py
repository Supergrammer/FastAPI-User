from fastapi import APIRouter

from app.configurations.settings import get_app_settings

router = APIRouter(
    prefix="/app",
    tags=["app"],
)


@router.get("/info")
def app_app_info():
    return get_app_settings()


@router.get("/health-check")
def health_check():
    return {"healthy": True}
