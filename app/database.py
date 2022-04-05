from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

POSTGRES_DATABASE_URL = "postgresql://fastapi_user:rlaguscjf@127.0.0.1/user_db"

engine = create_engine(POSTGRES_DATABASE_URL)

Session = sessionmaker(authcommit=False, autoflush=False, bind=engine)

Base = declarative_base