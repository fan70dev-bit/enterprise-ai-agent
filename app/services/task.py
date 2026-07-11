from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user import User


from app.crud.task import (
    create_task,
    get_task_by_id,
    list_tasks,
    list_user_tasks,
    update_task,
    delete_task,
)


from app.schemas.task import (
    TaskCreate,
    TaskUpdate,
)

from app.crud.task import (
    create_task as crud_create_task,
    get_task_by_title,
)



def create_task_service(
    db: Session,
    task: TaskCreate,
    current_user: User,
):

    old_task = get_task_by_title(
        db=db,
        user_id=current_user.id,
        title=task.title,
    )

    if old_task:
        return {
            "message": f"任务【{task.title}】已经存在，无需重复创建。"
        }

    task.user_id = current_user.id

    return crud_create_task(
        db=db,
        task=task,
    )



def get_task_service(
    db:Session,
    task_id:int
):

    task=get_task_by_id(
        db,
        task_id
    )

    if task is None:
        raise HTTPException(
            404,
            "Task not found"
        )

    return task



def list_tasks_service(
    db:Session
):

    return list_tasks(db)



def list_my_tasks_service(
    db:Session,
    user_id:int
):

    return list_user_tasks(
        db,
        user_id
    )



def update_task_service(
    db:Session,
    task_id:int,
    data:TaskUpdate
):

    task=get_task_service(
        db,
        task_id
    )

    return update_task(
        db,
        task,
        data
    )



def delete_task_service(
    db:Session,
    task_id:int
):

    task=get_task_service(
        db,
        task_id
    )

    delete_task(
        db,
        task
    )

