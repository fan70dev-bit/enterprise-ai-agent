from app.crud.task import (
    list_user_tasks,
    create_task as crud_create_task,
    get_task_by_title,
    update_task as crud_update_task,
)

from app.schemas.task import (
    TaskCreate,
    TaskUpdate,
)

from sqlalchemy.orm import Session

from app.crud.task import list_user_tasks
from app.crud.report import list_reports
from app.crud.user import get_user_by_id

from app.models.user import User



def get_my_tasks(
    db: Session,
    current_user: User,
):
    """
    获取当前用户任务
    """

    return list_user_tasks(
        db,
        current_user.id,
    )



def get_my_reports(
    db: Session,
    current_user: User,
):
    """
    获取当前用户日报
    """

    return list_reports(
        db,
    )



def get_user_info(
    db: Session,
    current_user: User,
):
    """
    获取当前用户信息
    """

    return get_user_by_id(
        db,
        current_user.id,
    )

def create_task(
    db: Session,
    current_user: User,
    title: str,
    description: str = "",
    priority: str = "medium",
):
    """
    创建任务
    """

    task = TaskCreate(
        title=title,
        description=description,
        status="todo",
        priority=priority,
        user_id=current_user.id,
    )

    return crud_create_task(
        db=db,
        task=task,
    )

def update_task(
    db: Session,
    current_user: User,
    title: str,
    status: str | None = None,
    priority: str | None = None,
):
    """
    修改任务
    """

    db_task = get_task_by_title(
        db=db,
        user_id=current_user.id,
        title=title,
    )

    if db_task is None:
        return "没有找到该任务。"

    task = TaskUpdate()

    if status is not None:
        task.status = status

    if priority is not None:
        task.priority = priority

    return crud_update_task(
        db=db,
        db_task=db_task,
        task=task,
    )