from sqlalchemy.orm import Session

from app.modules import auth_module

from .common import get_user_by_email


def authenticate_user(
    db: Session,
    email: str,
    password: str
):
    db_user = get_user_by_email(db=db, email=email)

    if not db_user or \
        not auth_module.verify_password(password, db_user.password.hashed_password):
        return False

    return db_user
