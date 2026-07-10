from sqlalchemy.orm import Session

from app.models.task import Task
from app.schemas.task import (
    TaskCreate,
    TaskUpdate,
)



def create_task(
    db: Session,
    task: TaskCreate
):

    db_task = Task(
        title=task.title,
        description=task.description,
        status=task.status,
        priority=task.priority,
        user_id=task.user_id,
    )


    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task



def get_task_by_id(
    db: Session,
    task_id: int
):

    return (
        db.query(Task)
        .filter(Task.id == task_id)
        .first()
    )



def list_tasks(
    db: Session
):

    return db.query(Task).all()



def list_user_tasks(
    db: Session,
    user_id:int
):

    return (
        db.query(Task)
        .filter(Task.user_id == user_id)
        .all()
    )

def list_tasks_by_user(
    db: Session,
    user_id: int,
):
    return (
        db.query(Task)
        .filter(Task.user_id == user_id)
        .all()
    )



def update_task(
    db: Session,
    db_task: Task,
    task: TaskUpdate
):

    data = task.model_dump(
        exclude_unset=True
    )

    for key,value in data.items():
        setattr(
            db_task,
            key,
            value
        )


    db.commit()
    db.refresh(db_task)

    return db_task



def delete_task(
    db: Session,
    db_task: Task
):

    db.delete(db_task)
    db.commit()

def get_task_by_title(
    db: Session,
    user_id: int,
    title: str,
):
    return (
        db.query(Task)
        .filter(
            Task.user_id == user_id,
            Task.title == title,
        )
        .first()
    )