from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.configurations.database import get_db
from app.modules import auth_module

from app.schemas import token_schema
from app.services import auth_service

from app.http_exception import invalid_user_exception

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

db = Depends(get_db)


@router.post("/login", response_model=token_schema.Response.TokenDetail)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = db
):
    db_user = auth_service.authenticate_user(
        db=db, email=form_data.username, password=form_data.password)

    if not db_user:
        raise invalid_user_exception

    return auth_module.get_token(db_user.email)


@router.post("/check")
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


@router.post("/refresh", response_model=token_schema.Response.TokenDetail)
async def refresh_access_token(
    token: token_schema.Request.TokenRefresh,
    current_user: str = Depends(auth_module.get_current_expired_user),
    db: Session = db
):
    return {}
