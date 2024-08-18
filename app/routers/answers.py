from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db_dependency
from typing import List


router = APIRouter()

@router.post("/answers", response_model=schemas.AnswerResponse)
def submit_answers(answers: List[schemas.AnswerCreate], db: Session = Depends(get_db_dependency)):
    return crud.submit_answers(db=db, answers=answers)
