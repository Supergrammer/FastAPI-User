from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

POSTGRES_DATABASE_URL = "postgresql://fastapi_user:rlaguscjf@127.0.0.1/user_db"

engine = create_engine(POSTGRES_DATABASE_URL)
db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()