from sqlalchemy.orm import Session
from app import models, schemas
from app.auth import get_password_hash
from fastapi import HTTPException
# CRUD functions for Board
def get_board(db: Session, board_id: int):
    return db.query(models.Board).filter(models.Board.id == board_id).first()

def get_boards(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Board).offset(skip).limit(limit).all()

def create_board(db: Session, board: schemas.BoardCreate):
    country = db.query(models.Country).filter(models.Country.country_code == board.country_code).first()
    if not country:
        raise HTTPException(status_code=400, detail="Country code does not exist.")
    db_board = models.Board(board_code=board.board_code, country_code=board.country_code, state=board.state)
    db.add(db_board)
    db.commit()
    db.refresh(db_board)
    return db_board

def delete_board(db: Session, board_id: int):
    db_board = db.query(models.Board).filter(models.Board.id == board_id).first()
    if db_board:
        db.delete(db_board)
        db.commit()

# CRUD functions for Language
def get_language(db: Session, language_id: int):
    return db.query(models.Language).filter(models.Language.id == language_id).first()

def get_languages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Language).offset(skip).limit(limit).all()

def create_language(db: Session, language: schemas.LanguageCreate):
    db_language = models.Language(language_name=language.language_name)
    db.add(db_language)
    db.commit()
    db.refresh(db_language)
    return db_language

def delete_language(db: Session, language_id: int):
    db_language = db.query(models.Language).filter(models.Language.id == language_id).first()
    if db_language:
        db.delete(db_language)
        db.commit()

# CRUD functions for Country
def get_country(db: Session, country_id: int):
    return db.query(models.Country).filter(models.Country.id == country_id).first()

def get_countries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Country).offset(skip).limit(limit).all()

def create_country(db: Session, country: schemas.CountryCreate):
    db_country = models.Country(country_name=country.country_name, country_code=country.country_code)
    db.add(db_country)
    db.commit()
    db.refresh(db_country)
    return db_country

def delete_country(db: Session, country_id: int):
    db_country = db.query(models.Country).filter(models.Country.id == country_id).first()
    if db_country:
        db.delete(db_country)
        db.commit()
        
# CRUD functions for State
def get_state(db: Session, state_id: int):
    return db.query(models.State).filter(models.State.id == state_id).first()

def get_states(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.State).offset(skip).limit(limit).all()

def create_state(db: Session, state: schemas.StateCreate):
    db_state = models.State(country_code=state.country_code, state_name=state.state_name, state_code=state.state_code)
    db.add(db_state)
    db.commit()
    db.refresh(db_state)
    return db_state

def delete_state(db: Session, state_id: int):
    db_state = db.query(models.State).filter(models.State.id == state_id).first()
    if db_state:
        db.delete(db_state)
        db.commit()

# CRUD functions for Class
def get_class(db: Session, class_id: int):
    return db.query(models.Class).filter(models.Class.id == class_id).first()

def get_classes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Class).offset(skip).limit(limit).all()

def create_class(db: Session, class_: schemas.ClassCreate):
    db_class = models.Class(class_code=class_.class_code, class_name=class_.class_name, board_code=class_.board_code)
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class

def delete_class(db: Session, class_id: int):
    db_class = db.query(models.Class).filter(models.Class.id == class_id).first()
    if db_class is None:
        return None
    db.delete(db_class)
    db.commit()
    return db_class

# CRUD functions for Subject
def get_subject(db: Session, subject_id: int):
    return db.query(models.Subject).filter(models.Subject.id == subject_id).first()

def get_subjects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Subject).offset(skip).limit(limit).all()

def create_subject(db: Session, subject: schemas.SubjectCreate):
    db_subject = models.Subject(subject_code=subject.subject_code, class_code=subject.class_code, subject_name=subject.subject_name, board_code=subject.board_code)
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject

def delete_subject(db: Session, subject_id: int):
    db_subject = db.query(models.Subject).filter(models.Subject.id == subject_id).first()
    if db_subject is None:
        return None
    db.delete(db_subject)
    db.commit()
    return db_subject

# CRUD functions for Chapter
def get_chapter(db: Session, chapter_id: int):
    return db.query(models.Chapter).filter(models.Chapter.id == chapter_id).first()

def get_chapters(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Chapter).offset(skip).limit(limit).all()

def create_chapter(db: Session, chapter: schemas.ChapterCreate):
    db_chapter = models.Chapter(chapter_code=chapter.chapter_code, subject_code=chapter.subject_code, class_code=chapter.class_code, chapter_name=chapter.chapter_name, board_code=chapter.board_code)
    db.add(db_chapter)
    db.commit()
    db.refresh(db_chapter)
    return db_chapter

def delete_chapter(db: Session, chapter_id: int):
    db_chapter = db.query(models.Chapter).filter(models.Chapter.id == chapter_id).first()
    if db_chapter is None:
        return None
    db.delete(db_chapter)
    db.commit()
    return db_chapter

# CRUD functions for ChapterContent
def get_chapter_content(db: Session, chapter_content_id: int):
    return db.query(models.ChapterContent).filter(models.ChapterContent.id == chapter_content_id).first()

def get_chapter_contents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ChapterContent).offset(skip).limit(limit).all()

def create_chapter_content(db: Session, chapter_content: schemas.ChapterContentCreate):
    db_chapter_content = models.ChapterContent(
        chapter_code=chapter_content.chapter_code, topic=chapter_content.topic,
        sub_topic=chapter_content.sub_topic, sub_sub_topic=chapter_content.sub_sub_topic,
        paragraph_number=chapter_content.paragraph_number, descriptive_content=chapter_content.descriptive_content,
        image_list=chapter_content.image_list, voice_generation_json=chapter_content.voice_generation_json
    )
    db.add(db_chapter_content)
    db.commit()
    db.refresh(db_chapter_content)
    return db_chapter_content

def delete_chapter_content(db: Session, chapter_content_id: int):
    db_chapter_content = db.query(models.ChapterContent).filter(models.ChapterContent.id == chapter_content_id).first()
    if db_chapter_content is None:
        return None
    db.delete(db_chapter_content)
    db.commit()
    return db_chapter_content

# CRUD functions for User
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()

# CRUD functions for Profile
def get_profile(db: Session, profile_id: int):
    return db.query(models.Profile).filter(models.Profile.profile_id == profile_id).first()

def get_profiles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Profile).offset(skip).limit(limit).all()

def create_profile(db: Session, profile: schemas.ProfileCreate):
    db_profile = models.Profile(
        user_id=profile.user_id, student_name=profile.student_name, age=profile.age,
        school_name=profile.school_name, board_id=profile.board_id
    )
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

def delete_profile(db: Session, profile_id: int):
    db_profile = db.query(models.Profile).filter(models.Profile.id == profile_id).first()
    if db_profile:
        db.delete(db_profile)
        db.commit()

# CRUD functions for Test
def get_test(db: Session, test_id: int):
    return db.query(models.Test).filter(models.Test.test_id == test_id).first()

def get_tests(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Test).offset(skip).limit(limit).all()

def create_test(db: Session, test: schemas.TestCreate):
    db_test = models.Test(topic_id=test.topic_id, type=test.type, description=test.description)
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test

def delete_test(db: Session, test_id: int):
    db_test = db.query(models.Test).filter(models.Test.id == test_id).first()
    if db_test:
        db.delete(db_test)
        db.commit()


# CRUD functions for TestResult
def get_test_result(db: Session, test_result_id: int):
    return db.query(models.TestResult).filter(models.TestResult.result_id == test_result_id).first()

def get_test_results(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TestResult).offset(skip).limit(limit).all()

def create_test_result(db: Session, test_result: schemas.TestResultCreate):
    db_test_result = models.TestResult(
        profile_id=test_result.profile_id, test_id=test_result.test_id, score=test_result.score,
        date_taken=test_result.date_taken, feedback=test_result.feedback
    )
    db.add(db_test_result)
    db.commit()
    db.refresh(db_test_result)
    return db_test_result

def delete_test_result(db: Session, test_result_id: int):
    db_test_result = db.query(models.TestResult).filter(models.TestResult.id == db_test_result).first()
    if db_test_result:
        db.delete(db_test_result)
        db.commit()

# CRUD functions for UserProgress
def get_user_progress(db: Session, user_progress_id: int):
    return db.query(models.UserProgress).filter(models.UserProgress.progress_id == user_progress_id).first()

def get_user_progresses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.UserProgress).offset(skip).limit(limit).all()

def create_user_progress(db: Session, user_progress: schemas.UserProgressCreate):
    db_user_progress = models.UserProgress(
        profile_id=user_progress.profile_id, subject_id=user_progress.subject_id,
        chapter_id=user_progress.chapter_id, topic_id=user_progress.topic_id,
        current=user_progress.current, last_accessed=user_progress.last_accessed,
        completed=user_progress.completed, completion_date=user_progress.completion_date
    )
    db.add(db_user_progress)
    db.commit()
    db.refresh(db_user_progress)
    return db_user_progress

def delete_user_progress(db: Session, user_progress_id: int):
    db_user_progress = db.query(models.UserProgress).filter(models.UserProgress.id == user_progress_id).first()
    if db_user_progress:
        db.delete(db_user_progress)
        db.commit()

# CRUD functions for ChapterProgress
def get_chapter_progress(db: Session, chapter_progress_id: int):
    return db.query(models.ChapterProgress).filter(models.ChapterProgress.chapter_progress_id == chapter_progress_id).first()

def get_chapter_progresses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ChapterProgress).offset(skip).limit(limit).all()

def create_chapter_progress(db: Session, chapter_progress: schemas.ChapterProgressCreate):
    db_chapter_progress = models.ChapterProgress(
        profile_id=chapter_progress.profile_id, chapter_id=chapter_progress.chapter_id,
        completed=chapter_progress.completed, completion_date=chapter_progress.completion_date
    )
    db.add(db_chapter_progress)
    db.commit()
    db.refresh(db_chapter_progress)
    return db_chapter_progress

def delete_chapter_progress(db: Session, chapter_progress_id: int):
    db_chapter_progress = db.query(models.ChapterProgress).filter(models.ChapterProgress.id == chapter_progress_id).first()
    if db_chapter_progress:
        db.delete(db_chapter_progress)
        db.commit()
        
# CRUD functions for TopicProgress
def get_topic_progress(db: Session, topic_progress_id: int):
    return db.query(models.TopicProgress).filter(models.TopicProgress.topic_progress_id == topic_progress_id).first()

def get_topic_progresses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TopicProgress).offset(skip).limit(limit).all()

def create_topic_progress(db: Session, topic_progress: schemas.TopicProgressCreate):
    db_topic_progress = models.TopicProgress(
        profile_id=topic_progress.profile_id, topic_id=topic_progress.topic_id,
        completed=topic_progress.completed, completion_date=topic_progress.completion_date
    )
    db.add(db_topic_progress)
    db.commit()
    db.refresh(db_topic_progress)
    return db_topic_progress

def delete_topic_progress(db: Session, topic_progress_id: int):
    db_topic_progress = db.query(models.TopicProgress).filter(models.TopicProgress.id == db_topic_progress).first()
    if db_topic_progress:
        db.delete(db_topic_progress)
        db.commit()
        

# CRUD functions for Certificate
def get_certificate(db: Session, certificate_id: int):
    return db.query(models.Certificate).filter(models.Certificate.certificate_id == certificate_id).first()

def get_certificates(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Certificate).offset(skip).limit(limit).all()

def create_certificate(db: Session, certificate: schemas.CertificateCreate):
    db_certificate = models.Certificate(
        result_id=certificate.result_id, issue_date=certificate.issue_date,
        certificate_url=certificate.certificate_url
    )
    db.add(db_certificate)
    db.commit()
    db.refresh(db_certificate)
    return db_certificate

def delete_certificate(db: Session, certificate_id: int):
    db_certificate = db.query(models.Certificate).filter(models.Certificate.id == certificate_id).first()
    if db_certificate:
        db.delete(db_certificate)
        db.commit()
                    