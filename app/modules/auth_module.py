from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

from fastapi import Depends, HTTPException, status

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

SECRET_KEY = "bf3514e276481e953c7191a61cf3bf858f572f166954681144f7718874f13945"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRATION_PERIOD = 2 * 60 * 60
REFRESH_TOKEN_EXPIRATION_PERIOD = 24 * 60 * 60

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

invalid_user_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect E-mail or Password.",
    headers={"WWW-Authenticate": "Bearer"}
)

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials.",
    headers={"WWW_Authenticate": "Bearer"}
)


def verify_password(plain_password, hashed_password):
    return password_context.verify(plain_password, hashed_password)


def get_hashed_password(plain_password):
    return password_context.hash(plain_password)


def create_token(data: dict, expiration_period: timedelta):
    expiration_datetime = datetime.utcnow() + expiration_period

    to_encode = data.copy()
    to_encode.update({"exp": expiration_datetime})

    access_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return access_token

def create_access_token(data: dict, expiration_period: timedelta = timedelta(seconds=ACCESS_TOKEN_EXPIRATION_PERIOD)):
    return create_token(data, expiration_period)

def create_refresh_token(data: dict, expiration_period: timedelta = timedelta(seconds=REFRESH_TOKEN_EXPIRATION_PERIOD)):
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
