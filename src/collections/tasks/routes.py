from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from src.collections.tasks.schemas import TaskCreate, TaskRead, TaskUpdate
from src.collections.tasks.service import create_task, delete_task, list_tasks, update_task
from src.collections.users.models import User
from src.database import get_db
from src.dependencies.auth import get_current_user


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("", response_model=list[TaskRead])
def get_tasks(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    return list_tasks(db, current_user.id)


@router.post("", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_new_task(
    payload: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_task(db, current_user.id, payload)


@router.put("/{task_id}", response_model=TaskRead)
def edit_task(
    task_id: int,
    payload: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return update_task(db, current_user.id, task_id, payload)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    delete_task(db, current_user.id, task_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
