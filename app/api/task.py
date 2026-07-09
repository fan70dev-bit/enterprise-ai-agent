from typing import List

from fastapi import APIRouter, Depends, Response, HTTPException
from sqlalchemy.orm import Session


from app.db.database import get_db

from app.core.deps import get_current_user

from app.models.user import User


from app.schemas.task import (
    TaskCreate,
    TaskUpdate,
    TaskResponse,
)


from app.services.task import (
    create_task_service,
    get_task_service,
    list_tasks_service,
    list_my_tasks_service,
    update_task_service,
    delete_task_service,
)



router = APIRouter(
    prefix="/tasks",
    tags=["Task"]
)



@router.post(
    "",
    response_model=TaskResponse
)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Only admin can create task"
        )


    return create_task_service(
        db,
        task
    )



@router.get(
    "",
    response_model=List[TaskResponse]
)
def list_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    if current_user.role == "admin":
        return list_tasks_service(db)


    return list_my_tasks_service(
        db,
        current_user.id
    )



@router.get(
    "/my",
    response_model=List[TaskResponse]
)
def my_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return list_my_tasks_service(
        db,
        current_user.id
    )



@router.get(
    "/{task_id}",
    response_model=TaskResponse
)
def get_task(
    task_id:int,
    db:Session = Depends(get_db),
    current_user:User = Depends(get_current_user)
):

    return get_task_service(
        db,
        task_id
    )



@router.put(
    "/{task_id}",
    response_model=TaskResponse
)
def update_task(
    task_id:int,
    data:TaskUpdate,
    db:Session=Depends(get_db),
    current_user:User=Depends(get_current_user)
):

    return update_task_service(
        db,
        task_id,
        data
    )



@router.delete(
    "/{task_id}",
    status_code=204
)
def delete_task_api(
    task_id:int,
    db:Session=Depends(get_db),
    current_user:User=Depends(get_current_user)
):

    delete_task_service(
        db,
        task_id
    )

    return Response(status_code=204)