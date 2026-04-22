from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.auth.schemas import LoginRequest, RegisterRequest, TokenResponse
from src.auth.services import login_user, register_user
from src.collections.users.schemas import UserRead
from src.database import get_db


router = APIRouter(tags=["auth"])


@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register(payload: RegisterRequest, db: Session = Depends(get_db)):
    return register_user(db, payload)


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    token = login_user(db, payload)
    return TokenResponse(access_token=token)
