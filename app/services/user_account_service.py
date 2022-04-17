from sqlalchemy.orm import Session

from app.models.user_model import User
from app.models.password_model import Password

from app.schemas import user_schema

from app.modules import auth_module


def create_user(db: Session, user: user_schema.Request.UserCreate):
    hashed_password = auth_module.get_hashed_password(user.password)

    db_user = User(
        email=user.email,
        password=Password(hashed_password=hashed_password),
        username=user.username,
        nickname=user.nickname
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def update_user(db: Session, email: str, user: user_schema.Request.UserCreate):
    db_user = get_user_by_email(db=db, email=email)

    db_user.username = user.username
    db_user.nickname = user.nickname

    db.commit()

    return db_user


def delete_user(db: Session, email: str):
    db_user = get_user_by_email(db=db, email=email)

    db.delete(db_user.password)
    db.delete(db_user)
    db.commit()

    return db_user
