from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.configurations.database import get_db
from app.services import user_auth_service

from app.schemas import user_schema

from app.modules import auth_module

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

db = Depends(get_db)


@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = db):
    db_user = user_auth_service.get_user(db=db, email=form_data.username)

    if not db_user:
        raise auth_module.invalid_user_exception

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

@router.post("/token/refresh")
async def refresh_access_token(current_user):
    pass


@router.get("/current", response_model=user_schema.User)
async def read_current_user(current_user: str = Depends(auth_module.get_current_user), db: Session = db):
    db_user = user_auth_service.get_user(db=db, email=current_user)

    if not db_user:
        raise auth_module.credentials_exception

    return db_user


@router.get("/current/active", response_model=user_schema.User)
async def read_current_active_user(current_user: str = Depends(auth_module.get_current_user), db: Session = db):
    db_user = user_auth_service.get_user(db=db, email=current_user)

    if not db_user or not db_user.is_active:
        raise auth_module.credentials_exception

    return db_user
