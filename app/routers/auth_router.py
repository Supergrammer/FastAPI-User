from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from aioredis import Redis

from app.configurations.user_database import get_user_db
from app.configurations.redis import get_redis_pool
from app.modules import auth_module

from app.schemas import token_schema
from app.services import auth_service
from app.services.common import get_user_by_email

from app.http_exception import invalid_user_exception, access_token_invalid_exception

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

db = Depends(get_user_db)
redis = Depends(get_redis_pool)


@router.post("/login", response_model=token_schema.Response.TokenDetail)
@router.post("/token", response_model=token_schema.Response.TokenDetail)
async def get_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = db,
    redis: Redis = redis
):
    db_user = auth_service.authenticate_user(
        db=db, email=form_data.username, password=form_data.password)

    if not db_user:
        raise invalid_user_exception

    return await auth_service.get_authentication(redis=redis, user=db_user)


@router.post("/token/refresh", response_model=token_schema.Response.TokenDetail)
async def refresh_token(
    token: token_schema.Request.TokenRefresh,
    expired_user: str = Depends(auth_module.get_all_user),
    db: Session = db,
    redis: Redis = redis
):
    db_user = get_user_by_email(db=db, email=expired_user)

    if not db_user:
        raise access_token_invalid_exception

    return await auth_service.refresh_authentication(redis=redis, user=db_user, refresh_token=token.refresh_token)


@router.post("/verify")
async def login_check(
    password: str,
    current_user: str = Depends(auth_module.get_current_user),
    db: Session = db
):
    db_user = auth_service.authenticate_user(
        db=db, email=current_user, password=password)

    if not db_user:
        raise invalid_user_exception

    return {}


@router.get("/logout")
async def logout(
    user: str = Depends(auth_module.get_all_user),
    db: Session = db,
    redis: Redis = redis
):
    db_user = get_user_by_email(db=db, email=user)

    if not db_user:
        raise access_token_invalid_exception

    await auth_service.expire_authentication(redis=redis, user=db_user)

    return {}
    