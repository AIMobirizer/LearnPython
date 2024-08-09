
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal
from typing import List

router = APIRouter(
    prefix="/certificates",
    tags=["certificates"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Certificate)
def create_certificate(certificate: schemas.CertificateCreate, db: Session = Depends(get_db)):
    return crud.create_certificate(db=db, certificate=certificate)

@router.get("/", response_model=List[schemas.Certificate])
def read_certificates(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    certificates = crud.get_certificates(db, skip=skip, limit=limit)
    return certificates

@router.get("/{certificate_id}", response_model=schemas.Certificate)
def read_certificate(certificate_id: int, db: Session = Depends(get_db)):
    db_certificate = crud.get_certificate(db, certificate_id=certificate_id)
    if db_certificate is None:
        raise HTTPException(status_code=404, detail="Certificate not found")
    return db_certificate
                