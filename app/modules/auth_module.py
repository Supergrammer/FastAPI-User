from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, jwt
from passlib.context import CryptContext

from datetime import datetime, timedelta

from app.configurations.settings import get_auth_module_settings
from app.http_exception import credentials_exception, password_match_exception

auth = get_auth_module_settings()

SECRET_KEY = auth.secret_key
ALGORITHM = auth.algorithm
ACCESS_TOKEN_EXPIRATION_PERIOD = auth.access_token_expiration_period
REFRESH_TOKEN_EXPIRATION_PERIOD = auth.refresh_token_expiration_period

PASSWORD_EXPIRATION_PERIOD = auth.password_expiration_period
PREVIOUS_PASSWORD_HISTORY_MATCH_COUNT = auth.previous_password_history_match_count

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def verify_password(plain_password, hashed_password):
    return password_context.verify(plain_password, hashed_password)


def get_hashed_password(plain_password):
    return password_context.hash(plain_password)


def check_previous_password_history(plain_password, password_history: list[str]):
    for history in password_history[:PREVIOUS_PASSWORD_HISTORY_MATCH_COUNT]:
        if verify_password(plain_password, history.hashed_password):
            raise password_match_exception


def create_token(data: dict, expiration_period: timedelta):
    expiration_datetime = datetime.utcnow() + expiration_period

    to_encode = data.copy()
    to_encode.update({"exp": expiration_datetime})

    access_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return access_token


def create_access_token(
    data: dict,
    expiration_period: timedelta = timedelta(
        milliseconds=ACCESS_TOKEN_EXPIRATION_PERIOD)
):
    return create_token(data, expiration_period)


def create_refresh_token(
    data: dict,
    expiration_period: timedelta = timedelta(
        milliseconds=REFRESH_TOKEN_EXPIRATION_PERIOD)
):
    return create_token(data, expiration_period)


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("e-mail")

        if email is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    return email
