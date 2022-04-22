from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.configurations.database import get_db
from app.modules import auth_module

from app.services import auth_service

from app.http_exception import invalid_user_exception

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

db = Depends(get_db)


@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = db
):
    db_user = auth_service.authenticate_user(
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


@router.post("/refresh")
async def refresh_access_token(
    current_user: str = Depends(auth_module.get_current_user),
    db: Session = db
):
    return {}
