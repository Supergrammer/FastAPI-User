from pydantic import BaseModel, UUID4, Field, validator
from datetime import datetime

from .base_schema import BaseSchema


class Password(BaseSchema):
    id: UUID4
    hashed_password: str
    is_expired: bool

    class Config:
        orm_mode = True


class Request():
    class PasswordUpdate(BaseModel):
        new_password: str
        confirm_password: str

        @validator("new_password")
        def new_password_validate(cls, v):
            return v

        @validator("confirm_password")
        def new_password_match(cls, v, values):
            if "new_password" in values and v != values["new_password"]:
                raise ValueError("새 비밀번호와 확인 비밀번호가 일치하지 않습니다.")
            return v

        class Config:
            orm_mode = True


class Response():
    class PasswordExpirationDate(BaseModel):
        updated_date: datetime = Field(alias="expiration_date")

        class Config:
            orm_mode = True
            allow_population_by_field_name = True
