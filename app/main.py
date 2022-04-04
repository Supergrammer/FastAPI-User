from typing import Optional
from unicodedata import name
from models import User

from fastapi import FastAPI

app = FastAPI()

import sqlalchemy

DATABASE_URL = "postgresql://fastapi_user:rlaguscjf@127.0.0.1/user_db"

@app.get("/")
def read_root():
    return {"item": 123123123}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}