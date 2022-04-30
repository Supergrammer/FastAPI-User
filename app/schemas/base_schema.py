from pydantic import BaseModel
from datetime import datetime


class BaseSchema(BaseModel):
    created_date: datetime
    updated_date: datetime
