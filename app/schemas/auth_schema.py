import email
from pydantic import BaseModel

class Token(BaseModel):
    token_type: str
    access_token: str

class TokenData(BaseModel):
    email: str | None = None
