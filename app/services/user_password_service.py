from sqlalchemy.orm import Session
from datetime import timedelta

from app.modules import auth_module

from app.models.password_history_model import PasswordHistory

from app.schemas import password_schema
from .common import get_user_by_email


def update_user_password(
    db: Session,
    current_user: str,
    password: password_schema.Request.PasswordUpdate
):
    db_user = get_user_by_email(db=db, email=current_user)

    password_history = db_user.password.password_history
    auth_module.check_previous_password_history(
        password.new_password, password_history)

    hashed_password = auth_module.get_hashed_password(password.new_password)

    password_history = PasswordHistory(
        id=db_user.password.id,
        hashed_password=hashed_password
    )

    db_user.password.hashed_password = hashed_password
    db_user.password.password_history.append(password_history)

    db.commit()

    return db_user


def get_expiration_date(
    db: Session,
    current_user: str
):
    db_user = get_user_by_email(db=db, email=current_user)

    updated_date = db_user.password.updated_date
    expiration_date = updated_date + \
        timedelta(seconds=auth_module.PASSWORD_EXPIRATION_PERIOD)

    return {"expiration_date": expiration_date}
