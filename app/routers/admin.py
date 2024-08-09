
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal
from typing import List

router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/insert_master_data")
def insert_master_data(db: Session = Depends(get_db)):
    # Insert sample data for boards
    board_data = [
        {"board_name": "CBSE", "country_code": "IN", "state": "Delhi"},
        {"board_name": "ICSE", "country_code": "IN", "state": "Delhi"}
    ]
    for data in board_data:
        board = schemas.BoardCreate(**data)
        crud.create_board(db, board)

    # Insert sample data for languages
    language_data = [
        {"language_name": "English"},
        {"language_name": "Hindi"}
    ]
    for data in language_data:
        language = schemas.LanguageCreate(**data)
        crud.create_language(db, language)

    # Insert sample data for countries
    country_data = [
        {"country_name": "India", "country_code": "IN"},
        {"country_name": "United States", "country_code": "US"}
    ]
    for data in country_data:
        country = schemas.CountryCreate(**data)
        crud.create_country(db, country)

    # Insert sample data for states
    state_data = [
        {"country_code": "IN", "state_name": "Delhi", "state_code": "DL"},
        {"country_code": "IN", "state_name": "Maharashtra", "state_code": "MH"}
    ]
    for data in state_data:
        state = schemas.StateCreate(**data)
        crud.create_state(db, state)

    return {"message": "Master data inserted successfully"}
                