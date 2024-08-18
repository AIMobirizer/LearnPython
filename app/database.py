
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# C:\Users\USER\Desktop\codegenereate\git_check\Backend_LearningApp\Backend_LearningApp\app\database.py
# Replace with your actual PostgreSQL credentials

# DATABASE_URL=postgres://postgress:Bong111BBB@prod2.c63jwtlancxa.ap-south-1.rds.amazonaws.com:5432/postgres
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:PostgresQl@learningapp.ch68meauc40x.ap-south-1.rds.amazonaws.com:5432/learningdb"

import sqlalchemy
# sqlalchemy.url = "postgresql://postgres:PostgresQl@learningapp.ch68meauc40x.ap-south-1.rds.amazonaws.com:5432/postgres"


# Create the PostgreSQL engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

