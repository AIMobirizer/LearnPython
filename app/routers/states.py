
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal
from typing import List

router = APIRouter(
    prefix="/states",
    tags=["states"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.State)
def create_state(state: schemas.StateCreate, db: Session = Depends(get_db)):
    return crud.create_state(db=db, state=state)

@router.get("/", response_model=List[schemas.State])
def read_states(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    states = crud.get_states(db, skip=skip, limit=limit)
    return states

@router.get("/{state_id}", response_model=schemas.State)
def read_state(state_id: int, db: Session = Depends(get_db)):
    db_state = crud.get_state(db, state_id=state_id)
    if db_state is None:
        raise HTTPException(status_code=404, detail="State not found")
    return db_state

@router.delete("/{state_id}", response_model=schemas.State)
def delete_state(state_id: int, db: Session = Depends(get_db)):
    db_state = crud.get_state(db, state_id=state_id)
    if db_state is None:
        raise HTTPException(status_code=404, detail="State not found")
    
    crud.delete_state(db, state_id=state_id)
    return db_state              