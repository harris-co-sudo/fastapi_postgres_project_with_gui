import time
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:postgres@db:5432/mydatabase"

# Retry DB connection
for _ in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        engine.connect()
        print("Database connected!")
        break
    except Exception as e:
        print("Database not ready, retrying...")
        time.sleep(3)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

def init_db():
    Base.metadata.create_all(bind=engine)
