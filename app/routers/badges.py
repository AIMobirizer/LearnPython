from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db_dependency, get_current_user_dependency
from typing import List


router = APIRouter()

@router.get("/badges", response_model=List[schemas.BadgeResponse])
def read_badges(db: Session = Depends(get_db_dependency), current_user: schemas.UserResponse = Depends(get_current_user_dependency)):
    return crud.get_badges(db)
