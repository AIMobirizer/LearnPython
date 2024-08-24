
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal
from typing import List

router = APIRouter(
    prefix="/classes",
    tags=["classes"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Class)
def create_class(class_: schemas.ClassCreate, db: Session = Depends(get_db)):
    return crud.create_class(db=db, class_=class_)

@router.get("/", response_model=List[schemas.Class])
def read_classes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    classes = crud.get_classes(db, skip=skip, limit=limit)
    return classes

@router.get("/{class_id}", response_model=schemas.Class)
def read_class(class_id: int, db: Session = Depends(get_db)):
    db_class = crud.get_class(db, class_id=class_id)
    if db_class is None:
        raise HTTPException(status_code=404, detail="Class not found")
    return db_class

@router.delete("/{class_id}", response_model=schemas.Class)
def delete_class(class_id: int, db: Session = Depends(get_db)):
    db_class = crud.delete_class(db, class_id=class_id)
    if db_class is None:
        raise HTTPException(status_code=404, detail="Class not found")
    return db_class                