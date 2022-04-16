from .base_schema import BaseSchema


class Password(BaseSchema):
    id: str
    password_hash: str
    is_expired: bool

    class Config:
        orm_mode = True
