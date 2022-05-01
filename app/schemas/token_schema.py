from pydantic import BaseModel


class TokenBase(BaseModel):
    pass


class Request():
    class TokenRefresh(TokenBase):
        refresh_token: str

        class Config():
            orm_mode = True


class Response():
    class TokenDetail(TokenBase):
        token_type: str
        access_token: str
        refresh_token: str
        expires_in: int

        class Config():
            orm_mode = True
