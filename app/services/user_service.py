from sqlalchemy.orm import Session

from app.modules import auth_module

from app.models.user_model import User
from app.models.password_model import Password
from app.models.password_history_model import PasswordHistory

from app.schemas import user_schema
from .common import get_user_by_email


def create_user(
    db: Session,
    user: user_schema.Request.UserCreate
):
    hashed_password = auth_module.get_hashed_password(user.password)

    db_user = User(
        email=user.email,
        username=user.username,
        nickname=user.nickname,

        password=Password(
            hashed_password=hashed_password,
            password_history=[
                PasswordHistory(hashed_password=hashed_password)
            ]
        )
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def update_user(
    db: Session,
    current_user: str,
    user: user_schema.Request.UserUpdate
):
    db_user = get_user_by_email(db=db, email=current_user)

    db_user.username = user.username
    db_user.nickname = user.nickname

    db.commit()

    return db_user


def delete_user(db: Session, current_user: str):
    db_user = get_user_by_email(db=db, email=current_user)

    db.delete(db_user)
    db.commit()

    return db_user
