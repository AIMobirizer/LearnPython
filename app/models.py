
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, DECIMAL, Text
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Board(Base):
    __tablename__ = "boards"
    id = Column(Integer, primary_key=True, index=True)
    board_code = Column(String, unique=True, index=True)
    country_code = Column(String, ForeignKey("countries.country_code"))
    state = Column(String)

    languages = relationship("BoardLanguage", back_populates="board")

class Language(Base):
    __tablename__ = "languages"
    id = Column(Integer, primary_key=True, index=True)
    language_name = Column(String, unique=True, index=True)

    boards = relationship("BoardLanguage", back_populates="language")

class BoardLanguage(Base):
    __tablename__ = "board_languages"
    board_code = Column(Integer, ForeignKey("boards.board_code"), primary_key=True)
    language_id = Column(Integer, ForeignKey("languages.id"), primary_key=True)

    board = relationship("Board", back_populates="languages")
    language = relationship("Language", back_populates="boards")

class Country(Base):
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True, index=True)
    country_name = Column(String)
    country_code = Column(String, unique=True, index=True)

class State(Base):
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, index=True)
    country_code = Column(String, ForeignKey("countries.country_code"))
    state_name = Column(String)
    state_code = Column(String, unique=True, index=True)

class Class(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True, index=True)
    class_code = Column(String, unique=True, index=True)
    class_name = Column(String)
    board_code = Column(String, ForeignKey("boards.board_code"))

# class Classes(Base):
#     __tablename__ = 'classes'

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     class_code = Column(String)
#     class_name = Column(String)
#     board_code = Column(String)
#     board = Column(Integer, ForeignKey('boards.board_code'))


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True, index=True)
    subject_code = Column(String, unique=True, index=True)
    class_code = Column(String, ForeignKey("classes.class_code"))
    subject_name = Column(String)
    board_code = Column(String, ForeignKey("boards.board_code"))

class Chapter(Base):
    __tablename__ = "chapters"
    id = Column(Integer, primary_key=True, index=True)
    chapter_code = Column(String, unique=True, index=True)
    subject_code = Column(String, ForeignKey("subjects.subject_code"))
    class_code = Column(String, ForeignKey("classes.class_code"))
    chapter_name = Column(String)
    board_code = Column(String, ForeignKey("boards.board_code"))

class ChapterContent(Base):
    __tablename__ = "chapter_contents"
    id = Column(Integer, primary_key=True, index=True)
    chapter_code = Column(String, ForeignKey("chapters.chapter_code"))
    topic = Column(String)
    sub_topic = Column(String)
    sub_sub_topic = Column(String)
    paragraph_number = Column(Integer)
    descriptive_content = Column(Text)
    image_list = Column(Text)  # Assuming JSON stored as Text
    voice_generation_json = Column(Text)  # Assuming JSON stored as Text

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime)

class Profile(Base):
    __tablename__ = "profiles"
    profile_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    student_name = Column(String)
    age = Column(Integer)
    school_name = Column(String)
    board_code = Column(Integer, ForeignKey("boards.board_code"))
    created_at = Column(DateTime, default=datetime.utcnow)

class Test(Base):
    __tablename__ = "tests"
    test_id = Column(Integer, primary_key=True, index=True)
    topic_id = Column(Integer, ForeignKey("chapter_contents.id"))
    type = Column(String)
    description = Column(Text)

class TestResult(Base):
    __tablename__ = "test_results"
    result_id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("profiles.profile_id"))
    test_id = Column(Integer, ForeignKey("tests.test_id"))
    score = Column(DECIMAL)
    date_taken = Column(DateTime, default=datetime.utcnow)
    feedback = Column(Text)

class UserProgress(Base):
    __tablename__ = "user_progress"
    progress_id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("profiles.profile_id"))
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    chapter_id = Column(Integer, ForeignKey("chapters.id"))
    topic_id = Column(Integer, ForeignKey("chapter_contents.id"))
    current = Column(Boolean)
    last_accessed = Column(DateTime)
    completed = Column(Boolean)
    completion_date = Column(DateTime)

class ChapterProgress(Base):
    __tablename__ = "chapter_progress"
    chapter_progress_id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("profiles.profile_id"))
    chapter_id = Column(Integer, ForeignKey("chapters.id"))
    completed = Column(Boolean)
    completion_date = Column(DateTime)

class TopicProgress(Base):
    __tablename__ = "topic_progress"
    topic_progress_id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("profiles.profile_id"))
    topic_id = Column(Integer, ForeignKey("chapter_contents.id"))
    completed = Column(Boolean)
    completion_date = Column(DateTime)

class Certificate(Base):
    __tablename__ = "certificates"
    certificate_id = Column(Integer, primary_key=True, index=True)
    result_id = Column(Integer, ForeignKey("test_results.result_id"))
    issue_date = Column(DateTime, default=datetime.utcnow)
    certificate_url = Column(String)
            