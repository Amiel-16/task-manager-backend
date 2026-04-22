from sqlalchemy.orm import Session

from src.collections.users.models import User
from src.collections.users.schemas import UserCreate
from src.core.security import hash_password


def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()


def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, user_in: UserCreate) -> User:
    user = User(email=user_in.email, password=hash_password(user_in.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
