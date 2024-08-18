# python
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import get_current_user
from app.models import User

def get_db_dependency(db: Session = Depends(get_db)):
    return db

def get_current_user_dependency(current_user: User = Depends(get_current_user)):
    return current_user
