from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

import uuid

from .base_model import Base, BaseMixin


class User(Base, BaseMixin):
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True,
                nullable=False, index=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False, index=True)
    password = relationship("Password", backref="user", uselist=False,
                            primaryjoin="foreign(User.id) == Password.id")
    username = Column(String, nullable=False)
    nickname = Column(String, nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)
