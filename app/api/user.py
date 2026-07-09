from typing import List

from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from app.core.deps import get_current_user
from app.db.database import get_db
from app.models.user import User

from app.schemas.user import (
    UserCreate,
    UserResponse,
    UserUpdate,
)

from app.services.user import (
    create_user_service,
    get_user_service,
    list_users_service,
    update_user_service,
    delete_user_service,
)

router = APIRouter(
    prefix="/users",
    tags=["User"],
)


@router.post(
    "",
    response_model=UserResponse,
)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_user_service(db, user)


@router.get(
    "",
    response_model=List[UserResponse],
)
def list_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return list_users_service(db)


@router.get(
    "/{user_id}",
    response_model=UserResponse,
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_user_service(db, user_id)


@router.put(
    "/{user_id}",
    response_model=UserResponse,
)
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return update_user_service(
        db,
        user_id,
        user,
    )


@router.delete(
    "/{user_id}",
    status_code=204,
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    delete_user_service(db, user_id)
    return Response(status_code=204)