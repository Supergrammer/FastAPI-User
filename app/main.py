from app.routers import user_account
from app.models import user_model
from app.configurations.database import engine

from fastapi import FastAPI

user_model.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(user_account.router)

@app.get("/")
def read_root():
    return {"item": 123123123}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
