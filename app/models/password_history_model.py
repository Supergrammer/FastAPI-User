from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

import uuid

from .base_model import Base, BaseMixin


class PasswordHistory(Base, BaseMixin):
    __tablename__ = "password_history"

    id = Column(UUID(as_uuid=True), primary_key=True,
                nullable=False, index=True, default=uuid.uuid4)
    hashed_password = Column(String, primary_key=True, nullable=False)
