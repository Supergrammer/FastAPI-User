from fastapi import FastAPI

from app.configurations.user_database import engine
from app.configurations.redis import init_redis_pool

from app.models import models
from app.routers import routers

models.Base.metadata.create_all(bind=engine)
init_redis_pool("localhost", "rlaguscjf123")

app = FastAPI()
app.include_router(router=routers.router)
