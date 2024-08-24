
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal
from typing import List

router = APIRouter(
    prefix="/chapters",
    tags=["chapters"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Chapter)
def create_chapter(chapter: schemas.ChapterCreate, db: Session = Depends(get_db)):
    return crud.create_chapter(db=db, chapter=chapter)

@router.get("/", response_model=List[schemas.Chapter])
def read_chapters(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    chapters = crud.get_chapters(db, skip=skip, limit=limit)
    return chapters

@router.get("/{chapter_id}", response_model=schemas.Chapter)
def read_chapter(chapter_id: int, db: Session = Depends(get_db)):
    db_chapter = crud.get_chapter(db, chapter_id=chapter_id)
    if db_chapter is None:
        raise HTTPException(status_code=404, detail="Chapter not found")
    return db_chapter

@router.delete("/{chapter_id}", response_model=schemas.Chapter)
def delete_chapter(chapter_id: int, db: Session = Depends(get_db)):
    db_chapter = crud.get_chapter(db, chapter_id=chapter_id)
    if db_chapter is None:
        raise HTTPException(status_code=404, detail="Chapter not found")
    
    crud.delete_chapter(db, chapter_id=chapter_id)
    return db_chapter                                    