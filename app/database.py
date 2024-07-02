from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# PostgreSQL credentials
POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = 'zxdews2'
POSTGRES_DB = 'healthvault'
POSTGRES_HOST = 'localhost'
POSTGRES_PORT = '5432'

SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:zxdews2@localhost:5432/healthvault"

Base = declarative_base()
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

