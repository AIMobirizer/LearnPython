
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal
from typing import List

router = APIRouter(
    prefix="/tests",
    tags=["tests"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Test)
def create_test(test: schemas.TestCreate, db: Session = Depends(get_db)):
    return crud.create_test(db=db, test=test)

@router.get("/", response_model=List[schemas.Test])
def read_tests(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tests = crud.get_tests(db, skip=skip, limit=limit)
    return tests

@router.get("/{test_id}", response_model=schemas.Test)
def read_test(test_id: int, db: Session = Depends(get_db)):
    db_test = crud.get_test(db, test_id=test_id)
    if db_test is None:
        raise HTTPException(status_code=404, detail="Test not found")
    return db_test

@router.delete("/{test_id}", response_model=schemas.Test)
def delete_test(test_id: int, db: Session = Depends(get_db)):
    db_test = crud.get_chapter(db, test_id=test_id)
    if db_test is None:
        raise HTTPException(status_code=404, detail="Test not found")
    
    crud.delete_chapter(db, test_id=test_id)
    return db_test                                                   