from pydantic import BaseModel
from datetime import datetime


class BaseSchema(BaseModel):
    created_date: datetime
    updated_date: datetime


class UserBase(BaseModel):
    email: str


class User(UserBase, BaseSchema):
    username: str
    nickname: str
    is_active: bool

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str
    username: str
    nickname: str

    class Config:
        orm_mode = True
