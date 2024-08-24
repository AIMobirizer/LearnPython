
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal
from typing import List

router = APIRouter(
    prefix="/languages",
    tags=["languages"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Language)
def create_language(language: schemas.LanguageCreate, db: Session = Depends(get_db)):
    return crud.create_language(db=db, language=language)

@router.get("/", response_model=List[schemas.Language])
def read_languages(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    languages = crud.get_languages(db, skip=skip, limit=limit)
    return languages

@router.get("/{language_id}", response_model=schemas.Language)
def read_language(language_id: int, db: Session = Depends(get_db)):
    db_language = crud.get_language(db, language_id=language_id)
    if db_language is None:
        raise HTTPException(status_code=404, detail="Language not found")
    return db_language
    
@router.delete("/{language_id}", response_model=schemas.Language)
def delete_language(language_id: int, db: Session = Depends(get_db)):
    db_language = crud.get_language(db, language_id=language_id)
    if db_language is None:
        raise HTTPException(status_code=404, detail="Language not found")
    
    crud.delete_language(db, language_id=language_id)
    return db_language            