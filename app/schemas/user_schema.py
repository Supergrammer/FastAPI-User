from pydantic import BaseModel, UUID4

from .base_schema import BaseSchema
from .password_schema import Password


class UserBase(BaseModel):
    email: str


class User(UserBase, BaseSchema):
    id: UUID4
    username: str
    nickname: str
    is_active: bool

    class Config:
        orm_mode = True

class UserAll(UserBase, BaseSchema):
    id: UUID4
    password: Password
    username: str
    nickname: str
    is_active: bool

    class Config:
        orm_mode = True


class Request():
    class UserCreate(BaseModel):
        email: str
        password: str
        username: str
        nickname: str

        class Config:
            orm_mode = True

    class UserUpdate(BaseModel):
        username: str
        nickname: str

        class Config:
            orm_mode = True

class Response():
    class UserRead(UserBase):
        username: str
        nickname: str
        is_active: bool
    
        class Config:
            orm_mode = True

    class UserReadDetail(UserBase, BaseSchema):
        id: UUID4
        username: str
        nickname: str
        is_active: bool

        class Config:
            orm_mode = True