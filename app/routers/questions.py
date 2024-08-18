from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db_dependency
from typing import List


router = APIRouter()

@router.get("/videos/{video_id}/questions", response_model=List[schemas.QuestionResponse])
def read_questions(video_id: int, db: Session = Depends(get_db_dependency)):
    return crud.get_questions_by_video(db, video_id=video_id)

@router.post("/questions", response_model=schemas.QuestionResponse)
def create_question(question: schemas.QuestionCreate, db: Session = Depends(get_db_dependency)):
    return crud.create_question(db=db, question=question)
