from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from .settings import get_database_settings

db = get_database_settings()

DATABASE_URL = f"{db.database}://{db.database_user}:{db.database_password}@{db.database_server}/{db.database_name}"

engine = create_engine(DATABASE_URL)
db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()
