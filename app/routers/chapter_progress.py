
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal
from typing import List

router = APIRouter(
    prefix="/chapter_progress",
    tags=["chapter_progress"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.ChapterProgress)
def create_chapter_progress(chapter_progress: schemas.ChapterProgressCreate, db: Session = Depends(get_db)):
    return crud.create_chapter_progress(db=db, chapter_progress=chapter_progress)

@router.get("/", response_model=List[schemas.ChapterProgress])
def read_chapter_progresses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    chapter_progresses = crud.get_chapter_progresses(db, skip=skip, limit=limit)
    return chapter_progresses

@router.get("/{chapter_progress_id}", response_model=schemas.ChapterProgress)
def read_chapter_progress(chapter_progress_id: int, db: Session = Depends(get_db)):
    db_chapter_progress = crud.get_chapter_progress(db, chapter_progress_id=chapter_progress_id)
    if db_chapter_progress is None:
        raise HTTPException(status_code=404, detail="ChapterProgress not found")
    return db_chapter_progress

@router.delete("/{chapter_progress_id}", response_model=schemas.ChapterProgress)
def delete_chapter_progress(chapter_progress_id: int, db: Session = Depends(get_db)):
    db_chapter_progress = crud.get_chapter_progress(db, chapter_progress_id=chapter_progress_id)
    if db_chapter_progress is None:
        raise HTTPException(status_code=404, detail="UserProgress not found")
    
    crud.delete_chapter_progress(db, chapter_progress_id=chapter_progress_id)
    return db_chapter_progress                   