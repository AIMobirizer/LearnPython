
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal
from typing import List

router = APIRouter(
    prefix="/user_progress",
    tags=["user_progress"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.UserProgress)
def create_user_progress(user_progress: schemas.UserProgressCreate, db: Session = Depends(get_db)):
    return crud.create_user_progress(db=db, user_progress=user_progress)

@router.get("/", response_model=List[schemas.UserProgress])
def read_user_progresses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    user_progresses = crud.get_user_progresses(db, skip=skip, limit=limit)
    return user_progresses

@router.get("/{user_progress_id}", response_model=schemas.UserProgress)
def read_user_progress(user_progress_id: int, db: Session = Depends(get_db)):
    db_user_progress = crud.get_user_progress(db, user_progress_id=user_progress_id)
    if db_user_progress is None:
        raise HTTPException(status_code=404, detail="UserProgress not found")
    return db_user_progress

@router.delete("/{user_progress_id}", response_model=schemas.UserProgress)
def delete_user_progress(user_progress_id: int, db: Session = Depends(get_db)):
    db_user_progress = crud.get_chapter(db, user_progress_id=user_progress_id)
    if db_user_progress is None:
        raise HTTPException(status_code=404, detail="UserProgress not found")
    
    crud.delete_chapter(db, user_progress_id=user_progress_id)
    return db_user_progress                 