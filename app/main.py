from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal, init_db, User
from app.models import UserCreate
<<<<<<< HEAD
from dotenv import load_dotenv
import os

load_dotenv(".env")  # ensures the .env file is loaded
=======
>>>>>>> 0dd640e5d8c651b23214946664adddcfcc3a3a3d

app = FastAPI()

# Initialize DB
init_db()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()
