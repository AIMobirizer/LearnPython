
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal
from typing import List

router = APIRouter(
    prefix="/boards",
    tags=["boards"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Board)
def create_board(board: schemas.BoardCreate,db: Session = Depends(get_db)):
    return crud.create_board(db=db, board=board)


@router.get("/", response_model=List[schemas.Board])
def read_boards(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    boards = crud.get_boards(db, skip=skip, limit=limit)
    return boards


@router.get("/{board_id}", response_model=schemas.Board)
def read_board(board_id: int, db: Session = Depends(get_db)):
    db_board = crud.get_board(db, board_id=board_id)
    
    if db_board is None:
        raise HTTPException(status_code=404, detail="Board not found")
    return db_board
                