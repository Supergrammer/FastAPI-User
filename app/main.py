from fastapi import FastAPI

from app.routers import routers
from app.models import models
from app.configurations.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router=routers.router)
