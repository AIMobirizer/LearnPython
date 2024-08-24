
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal
from typing import List

router = APIRouter(
    prefix="/chapter_contents",
    tags=["chapter_contents"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.ChapterContent)
def create_chapter_content(chapter_content: schemas.ChapterContentCreate, db: Session = Depends(get_db)):
    return crud.create_chapter_content(db=db, chapter_content=chapter_content)

@router.get("/", response_model=List[schemas.ChapterContent])
def read_chapter_contents(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    chapter_contents = crud.get_chapter_contents(db, skip=skip, limit=limit)
    return chapter_contents

@router.get("/{chapter_content_id}", response_model=schemas.ChapterContent)
def read_chapter_content(chapter_content_id: int, db: Session = Depends(get_db)):
    db_chapter_content = crud.get_chapter_content(db, chapter_content_id=chapter_content_id)
    if db_chapter_content is None:
        raise HTTPException(status_code=404, detail="ChapterContent not found")
    return db_chapter_content

@router.delete("/{chapter_content_id}", response_model=schemas.ChapterContent)
def delete_chapter_content(chapter_content_id: int, db: Session = Depends(get_db)):
    db_chapter_content = crud.get_chapter_content(db, chapter_content_id=chapter_content_id)
    if db_chapter_content is None:
        raise HTTPException(status_code=404, detail="ChapterContent not found")
    
    crud.delete_chapter_content(db, chapter_content_id=chapter_content_id)
    return db_chapter_content                    