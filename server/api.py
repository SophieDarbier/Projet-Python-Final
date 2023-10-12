from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from . import models
from .database import SessionLocal, engine

app = FastAPI()

# Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}


