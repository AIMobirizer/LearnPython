from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db_dependency
from typing import List

router = APIRouter()

@router.get("/technologies/{tech_id}/topics", response_model=List[schemas.TopicResponse])
def read_topics(tech_id: int, db: Session = Depends(get_db_dependency)):
    return crud.get_topics_by_technology(db, technology_id=tech_id)

@router.post("/topics", response_model=schemas.TopicResponse)
def create_topic(topic: schemas.TopicCreate, db: Session = Depends(get_db_dependency)):
    return crud.create_topic(db=db, topic=topic)
