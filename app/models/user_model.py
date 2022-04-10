from sqlalchemy import Column, String, Boolean

from .base_model import Base, BaseMixin


class User(Base, BaseMixin):
    __tablename__ = "user"

    email = Column(String, primary_key=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    username = Column(String, nullable=False)
    nickname = Column(String, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
