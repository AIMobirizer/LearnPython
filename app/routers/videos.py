from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db_dependency
from typing import List


router = APIRouter()

@router.get("/topics/{topic_id}/videos", response_model=List[schemas.VideoResponse])
def read_videos(topic_id: int, db: Session = Depends(get_db_dependency)):
    return crud.get_videos_by_topic(db, topic_id=topic_id)

@router.post("/videos", response_model=schemas.VideoResponse)
def create_video(video: schemas.VideoCreate, db: Session = Depends(get_db_dependency)):
    return crud.create_video(db=db, video=video)
