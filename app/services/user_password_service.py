from sqlalchemy.orm import Session

from app.modules import auth_module

from app.models.user_model import User
from app.models.password_model import Password
from app.models.password_history_model import PasswordHistory

from app.schemas import user_schema, password_schema

from app.http_exception import bad_request


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def update_user_password(db: Session, current_user: str, password: password_schema.Request.PasswordUpdate):
    db_user = get_user_by_email(db=db, email=current_user)

    if not auth_module.verify_password(password.current_password, db_user.password.hashed_password):
        raise bad_request

    hashed_password = auth_module.get_hashed_password(password.new_password)

    password_history = PasswordHistory(
        id=db_user.password.id,
        hashed_password=hashed_password
    )

    db_user.password.hashed_password = hashed_password
    db_user.password.password_history.append(password_history)

    db.commit()

    return db_user
