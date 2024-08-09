
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from app.routers import (
    users, boards, languages, countries, states, classes, subjects,
    chapters, chapter_contents, profiles, tests, test_results, user_progress,
    chapter_progress, topic_progress, certificates, admin
)
from app.database import engine, SessionLocal
from app import models, schemas, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(boards.router)
app.include_router(languages.router)
app.include_router(countries.router)
app.include_router(states.router)
app.include_router(classes.router)
app.include_router(subjects.router)
app.include_router(chapters.router)
app.include_router(chapter_contents.router)
app.include_router(profiles.router)
app.include_router(tests.router)
app.include_router(test_results.router)
app.include_router(user_progress.router)
app.include_router(chapter_progress.router)
app.include_router(topic_progress.router)
app.include_router(certificates.router)
app.include_router(admin.router)

@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(SessionLocal)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


import uvicorn
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8083, reload=True)
