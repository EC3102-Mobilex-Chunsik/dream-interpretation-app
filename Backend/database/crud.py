from sqlalchemy.orm import Session
import models
import schemas

# User 관련 함수들


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(
        email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Item 관련 함수들


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Dream 관련 함수들


def get_dream(db: Session, dream_id: int):
    return db.query(models.Dream).filter(models.Dream.id == dream_id).first()


def get_dreams(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Dream).offset(skip).limit(limit).all()


def create_dream(db: Session, dream: schemas.DreamCreate):
    db_dream = models.Dream(
        dateTime=dream.dateTime,
        title=dream.title,
        inputPrompt=dream.inputPrompt,
        context=dream.context
    )
    db.add(db_dream)
    db.commit()
    db.refresh(db_dream)

    for factor in dream.factors:
        db_factor = models.DreamFactor(
            dream_id=db_dream.id,
            tagName=factor.tagName,
            description=factor.description
        )
        db.add(db_factor)

    for image in dream.images:
        db_image = models.DreamImage(
            dream_id=db_dream.id,
            url=image.url
        )
        db.add(db_image)

    db.commit()

    return db_dream


def get_dream_factors(db: Session, dream_id: int):
    return db.query(models.DreamFactor).filter(models.DreamFactor.dream_id == dream_id).all()


def get_dream_images(db: Session, dream_id: int):
    return db.query(models.DreamImage).filter(models.DreamImage.dream_id == dream_id).all()
