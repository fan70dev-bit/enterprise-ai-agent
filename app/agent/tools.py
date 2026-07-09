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