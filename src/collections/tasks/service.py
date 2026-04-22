from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.collections.tasks.models import Task
from src.collections.tasks.schemas import TaskCreate, TaskUpdate


def list_tasks(db: Session, user_id: int) -> list[Task]:
    return db.query(Task).filter(Task.user_id == user_id).all()


def create_task(db: Session, user_id: int, task_in: TaskCreate) -> Task:
    task = Task(text=task_in.text, done=task_in.done, user_id=user_id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def update_task(db: Session, user_id: int, task_id: int, task_in: TaskUpdate) -> Task:
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == user_id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    if task_in.text is not None:
        task.text = task_in.text
    if task_in.done is not None:
        task.done = task_in.done

    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, user_id: int, task_id: int) -> None:
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == user_id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    db.delete(task)
    db.commit()
