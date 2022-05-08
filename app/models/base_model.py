from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func

from app.configurations.user_database import Base


class BaseMixin():
    created_date = Column(DateTime(timezone=True),
                          default=func.now(), nullable=False)
    updated_date = Column(DateTime(timezone=True),
                          default=func.now(), onupdate=func.now(), nullable=False)
