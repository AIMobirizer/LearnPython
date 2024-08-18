from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db_dependency
from typing import List

router = APIRouter()

@router.get("/technologies", response_model=List[schemas.TechnologyResponse])
def read_technologies(db: Session = Depends(get_db_dependency)):
    return crud.get_technologies(db)

@router.post("/technologies", response_model=schemas.TechnologyResponse)
def create_technology(technology: schemas.TechnologyCreate, db: Session = Depends(get_db_dependency)):
    return crud.create_technology(db=db, technology=technology)
