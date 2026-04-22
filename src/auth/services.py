from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.auth.schemas import LoginRequest, RegisterRequest
from src.collections.users.schemas import UserCreate
from src.collections.users.services import create_user, get_user_by_email
from src.core.security import create_access_token, verify_password


def register_user(db: Session, payload: RegisterRequest):
    existing = get_user_by_email(db, payload.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    return create_user(db, UserCreate(email=payload.email, password=payload.password))


def login_user(db: Session, payload: LoginRequest) -> str:
    user = get_user_by_email(db, payload.email)
    if not user or not verify_password(payload.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )
    return create_access_token(str(user.id))
