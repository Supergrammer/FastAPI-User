from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID

import uuid

from .base_model import Base, BaseMixin


class Password(Base, BaseMixin):
    __tablename__ = "password"

    id = Column(UUID(as_uuid=True), primary_key=True,
                nullable=False, index=True, default=uuid.uuid4)
    hashed_password = Column(String, nullable=False)
    is_expired = Column(Boolean, nullable=False, default=False)
