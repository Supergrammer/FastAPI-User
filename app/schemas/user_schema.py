from pydantic import BaseModel, UUID4, EmailStr, validator
import re

from .base_schema import BaseSchema
from .password_schema import Password


class UserBase(BaseModel):
    email: EmailStr


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
        email: EmailStr
        password: str
        username: str
        nickname: str

        @validator("password")
        def new_password_validate(cls, v):
            password_regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()=+]).{8,}$"
            assert re.findall(
                password_regex, v), "비밀번호는 8자 이상의 영문, 숫자, 특수문자로 구성되어야 합니다."
            return v

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
