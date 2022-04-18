from pydantic import BaseModel, UUID4, validator

from .base_schema import BaseSchema


class Password(BaseSchema):
    id: UUID4
    hashed_password: str
    is_expired: bool

    class Config:
        orm_mode = True


class Request():
    class PasswordUpdate(BaseModel):
        current_password: str
        new_password: str
        confirm_password: str

        @validator("new_password")
        def new_password_validate(cls, v, values):
            if "current_password" in values and v == values["current_password"]:
                raise ValueError("입력한 비밀번호와 바꾸려는 비밀번호가 동일합니다.")
            return v

        @validator("confirm_password")
        def password_match(cls, v, values):
            if "new_password" in values and v != values["new_password"]:
                raise ValueError("새 비밀번호와 확인 비밀번호가 일치하지 않습니다.")
            return v

        class Config:
            orm_mode = True
