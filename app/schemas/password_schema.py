from pydantic import UUID4

from .base_schema import BaseSchema


class Password(BaseSchema):
    id: UUID4
    hashed_password: str
    is_expired: bool

    class Config:
        orm_mode = True
