from fastapi import FastAPI

from app.configurations.database import engine

from app.models import models
from app.routers import routers

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router=routers.router)
