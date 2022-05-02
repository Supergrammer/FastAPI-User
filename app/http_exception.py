from fastapi import HTTPException, status

user_already_exist_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="E-mail already exists."
)

user_not_exist_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="E-mail does not exist."
)

password_match_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="새로운 비밀번호가 이전 3개의 비밀번호와 같습니다."
)

bad_request = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Bad request."
)

refresh_token_invalid_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="유효하지 않은 refresh_token 을 이용한 요청입니다.",
    headers={"WWW-Authenticate": "Bearer"}
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
