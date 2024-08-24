
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal
from typing import List

router = APIRouter(
    prefix="/topic_progress",
    tags=["topic_progress"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.TopicProgress)
def create_topic_progress(topic_progress: schemas.TopicProgressCreate, db: Session = Depends(get_db)):
    return crud.create_topic_progress(db=db, topic_progress=topic_progress)

@router.get("/", response_model=List[schemas.TopicProgress])
def read_topic_progresses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    topic_progresses = crud.get_topic_progresses(db, skip=skip, limit=limit)
    return topic_progresses

@router.get("/{topic_progress_id}", response_model=schemas.TopicProgress)
def read_topic_progress(topic_progress_id: int, db: Session = Depends(get_db)):
    db_topic_progress = crud.get_topic_progress(db, topic_progress_id=topic_progress_id)
    if db_topic_progress is None:
        raise HTTPException(status_code=404, detail="TopicProgress not found")
    return db_topic_progress

@router.delete("/{topic_progress_id}", response_model=schemas.TopicProgress)
def delete_topic_progress(topic_progress_id: int, db: Session = Depends(get_db)):
    db_topic_progress = crud.get_topic_progress(db, topic_progress_id=topic_progress_id)
    if db_topic_progress is None:
        raise HTTPException(status_code=404, detail="TopicProgress not found")
    
    crud.delete_topic_progress(db, db_topic_progress=topic_progress_id)
    return db_topic_progress                  