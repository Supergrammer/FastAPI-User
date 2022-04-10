from sqlalchemy.orm import Session

from app.models.user_model import User
from app.schemas import user_schema


def create_user(db: Session, user: user_schema.UserCreate):
    password = "hashedPassword"

    db_user = User(email=user.email, password=password,
                   username=user.username, nickname=user.nickname)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user(db: Session, email: str):
    return db.query(User).get(email)


def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def update_user(db: Session, user: user_schema.UserCreate):
    db_user = get_user(db=db, email=user.email)

    db_user.password = user.password
    db_user.username = user.username
    db_user.nickname = user.nickname

    db.commit()

    return db_user


def delete_user(db: Session, email: str):
    db_user = get_user(db=db, email=email)

    db.delete(db_user)
    db.commit()

    return db_user
