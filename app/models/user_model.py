from unicodedata import name
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from app.configurations.database import Base

class User(Base):
    __tablename__ = "user"

    email = Column(String, primary_key=True, index=True)
    hashed_password = Column(String)
    username = Column(String)
    nickname = Column(String)
    is_active = Column(Boolean, default=True)