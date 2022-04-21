from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.configurations.database import get_db
from app.services import user_auth_service

from app.schemas import user_schema

from app.modules import auth_module

from app.http_exception import invalid_user_exception, credentials_exception

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

db = Depends(get_db)


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = db):
    db_user = user_auth_service.authenticate_user(
        db=db, email=form_data.username, password=form_data.password)

    if not db_user:
        raise invalid_user_exception

    access_token = auth_module.create_access_token(data={
        "e-mail": db_user.email
    })

    refresh_token = auth_module.create_refresh_token(data={
        "e-mail": db_user.email
    })

    return {
        "token_type": "Bearer",
        "access_token": access_token,
        "refresh_token": refresh_token
    }


@router.post("/login/check")
async def login_check(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = db):
    db_user = user_auth_service.authenticate_user(
        db=db, email=form_data.username, password=form_data.password)

    if not db_user:
        raise invalid_user_exception

    return {}


@router.post("/login/refresh")
async def refresh_access_token(current_user):
    pass

