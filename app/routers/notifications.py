from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db_dependency, get_current_user_dependency
from typing import List


router = APIRouter()

@router.get("/notifications", response_model=List[schemas.NotificationResponse])
def read_notifications(db: Session = Depends(get_db_dependency), current_user: schemas.UserResponse = Depends(get_current_user_dependency)):
    return crud.get_notifications_by_user(db, user_id=current_user.id)

@router.post("/notifications/read", response_model=schemas.NotificationResponse)
def mark_notification_as_read(notification_id: int, db: Session = Depends(get_db_dependency), current_user: schemas.UserResponse = Depends(get_current_user_dependency)):
    return crud.mark_notification_as_read(db=db, notification_id=notification_id)
