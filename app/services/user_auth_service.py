from sqlalchemy.orm import Session

from app.models.user_model import User

from app.modules import auth_module


def get_user(db: Session, email: str):
    return db.query(User).get(email)


def authenticate_user(db: Session, email: str, password: str):
    db_user = get_user(db=db, email=email)

    if not db_user:
        return False
    if not auth_module.verify_password(password, db_user.password):
        return False

    return db_user