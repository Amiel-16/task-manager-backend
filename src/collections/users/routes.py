from fastapi import APIRouter, Depends

from src.collections.users.models import User
from src.collections.users.schemas import UserRead
from src.dependencies.auth import get_current_user


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserRead)
def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user

@router.get("/id", response_model=int)
def read_current_user_id(current_user: User = Depends(get_current_user)):
    return current_user.id
