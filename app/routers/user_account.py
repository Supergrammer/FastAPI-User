from fastapi import APIRouter

router = APIRouter(
    prefix="/user",
    tags=["user"],
)

@router.post("")
async def create_user():
    return {"123123": 25125205}

@router.get("")
async def read_user():
    return {"123": 123123}

@router.put("")
async def update_user():
    return {}

@router.delete("")
async def delete_user():
    return {}