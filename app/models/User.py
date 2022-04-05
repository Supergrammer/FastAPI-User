from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from app.database import Base


class User(Base):
    __tablename__ = "user"

    email = Column(String, primary_key=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)