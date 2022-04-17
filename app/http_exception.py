from fastapi import HTTPException, status

user_already_exist_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="E-mail already exists."
)

user_not_exist_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="E-mail does not exist."
)

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
