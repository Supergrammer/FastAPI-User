from sqlalchemy.orm import Session

from app.models.user_model import User
from app.schemas.user_schema import User as user

def create_user(db: Session, email: str):
    return db.query(User).filter(User.email == email).all()

def read_user():
    return {"123": 123123}

def update_user():
    return {}

def delete_user():
    return {}