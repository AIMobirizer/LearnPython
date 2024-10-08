
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BoardBase(BaseModel):
    board_code: str
    country_code: str
    state: str

class BoardCreate(BoardBase):
    pass

class Board(BoardBase):
    id: int

    class Config:
        orm_mode = True

class LanguageBase(BaseModel):
    language_name: str

class LanguageCreate(LanguageBase):
    pass

class Language(LanguageBase):
    id: int

    class Config:
        orm_mode = True

class CountryBase(BaseModel):
    country_name: str
    country_code: str

class CountryCreate(CountryBase):
    pass

class Country(CountryBase):
    id: int

    class Config:
        orm_mode = True

class StateBase(BaseModel):
    country_code: str
    state_name: str
    state_code: str

class StateCreate(StateBase):
    pass

class State(StateBase):
    id: int

    class Config:
        orm_mode = True

class ClassBase(BaseModel):
    class_code: str
    class_name: str
    board_code: str

class ClassCreate(ClassBase):
    pass

class Class(ClassBase):
    id: int

    class Config:
        orm_mode = True

class SubjectBase(BaseModel):
    subject_code: str
    class_code: str
    subject_name: str
    board_code: str

class SubjectCreate(SubjectBase):
    pass

class Subject(SubjectBase):
    id: int

    class Config:
        orm_mode = True

class ChapterBase(BaseModel):
    chapter_code: str
    subject_code: str
    class_code: str
    chapter_name: str
    board_code: str

class ChapterCreate(ChapterBase):
    pass

class Chapter(ChapterBase):
    id: int

    class Config:
        orm_mode = True

class ChapterContentBase(BaseModel):
    chapter_code: str
    topic: str
    sub_topic: Optional[str] = None
    sub_sub_topic: Optional[str] = None
    paragraph_number: Optional[int] = None
    descriptive_content: Optional[str] = None
    image_list: Optional[str] = None
    voice_generation_json: Optional[str] = None

class ChapterContentCreate(ChapterContentBase):
    pass

class ChapterContent(ChapterContentBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    last_login: Optional[datetime] = None

    class Config:
        orm_mode = True

class ProfileBase(BaseModel):
    user_id: int
    student_name: str
    age: int
    school_name: str
    board_code: str

class ProfileCreate(ProfileBase):
    pass

class Profile(ProfileBase):
    profile_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class TestBase(BaseModel):
    topic_id: int
    type: str
    description: Optional[str] = None

class TestCreate(TestBase):
    pass

class Test(TestBase):
    test_id: int

    class Config:
        orm_mode = True

class TestResultBase(BaseModel):
    profile_id: int
    test_id: int
    score: float
    date_taken: Optional[datetime] = None
    feedback: Optional[str] = None

class TestResultCreate(TestResultBase):
    pass

class TestResult(TestResultBase):
    result_id: int

    class Config:
        orm_mode = True

class UserProgressBase(BaseModel):
    profile_id: int
    subject_id: int
    chapter_id: int
    topic_id: int
    current: bool
    last_accessed: Optional[datetime] = None
    completed: Optional[bool] = None
    completion_date: Optional[datetime] = None

class UserProgressCreate(UserProgressBase):
    pass

class UserProgress(UserProgressBase):
    progress_id: int

    class Config:
        orm_mode = True

class ChapterProgressBase(BaseModel):
    profile_id: int
    chapter_id: int
    completed: Optional[bool] = None
    completion_date: Optional[datetime] = None

class ChapterProgressCreate(ChapterProgressBase):
    pass

class ChapterProgress(ChapterProgressBase):
    chapter_progress_id: int

    class Config:
        orm_mode = True

class TopicProgressBase(BaseModel):
    profile_id: int
    topic_id: int
    completed: Optional[bool] = None
    completion_date: Optional[datetime] = None

class TopicProgressCreate(TopicProgressBase):
    pass

class TopicProgress(TopicProgressBase):
    topic_progress_id: int

    class Config:
        orm_mode = True

class CertificateBase(BaseModel):
    result_id: int
    issue_date: datetime
    certificate_url: str

class CertificateCreate(CertificateBase):
    pass

class Certificate(CertificateBase):
    certificate_id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
            