
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal
from typing import List

router = APIRouter(
    prefix="/test_results",
    tags=["test_results"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.TestResult)
def create_test_result(test_result: schemas.TestResultCreate, db: Session = Depends(get_db)):
    return crud.create_test_result(db=db, test_result=test_result)

@router.get("/", response_model=List[schemas.TestResult])
def read_test_results(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    test_results = crud.get_test_results(db, skip=skip, limit=limit)
    return test_results

@router.get("/{test_result_id}", response_model=schemas.TestResult)
def read_test_result(test_result_id: int, db: Session = Depends(get_db)):
    db_test_result = crud.get_test_result(db, test_result_id=test_result_id)
    if db_test_result is None:
        raise HTTPException(status_code=404, detail="TestResult not found")
    return db_test_result

@router.delete("/{test_result_id}", response_model=schemas.TestResult)
def delete_test_result(test_result_id: int, db: Session = Depends(get_db)):
    db_test_result = crud.get_chapter(db, test_result_id=test_result_id)
    if db_test_result is None:
        raise HTTPException(status_code=404, detail="TestResult not found")
    
    crud.delete_chapter(db, test_result_id=test_result_id)
    return db_test_result                 