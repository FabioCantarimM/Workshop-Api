from sqlalchemy.exc import ArgumentError
from sqlalchemy.orm import Session

from src.models import models, schemas


def get_user(
    db: Session,
    user_id: int | None = None,
    email: str | None = None,
):
    if not any([user_id, email]):
        raise ArgumentError("Must provide user_id or email.")

    query = db.query(models.User)
    if user_id:
        query = query.filter(models.User.id == user_id)
    if email:
        query = query.filter(models.User.email == email)

    return query.first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        email=user.email,
        hashed_password=get_password_hash(user.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Item)
        .where(models.Item.owner_id == user_id)
        .offset(skip)
        .limit(limit)
        .all()
    )
