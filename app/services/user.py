from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.crud.user import (
    create_user,
    delete_user,
    get_user_by_id,
    get_user_by_username,
    list_users,
    update_user,
)

from app.schemas.user import (
    UserCreate,
    UserUpdate,
)


def create_user_service(
    db: Session,
    user: UserCreate,
):
    if get_user_by_username(db, user.username):
        raise HTTPException(
            status_code=400,
            detail="Username already exists",
        )

    return create_user(db, user)


def get_user_service(
    db: Session,
    user_id: int,
):
    db_user = get_user_by_id(db, user_id)

    if db_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return db_user


def list_users_service(db: Session):
    return list_users(db)


def update_user_service(
    db: Session,
    user_id: int,
    user: UserUpdate,
):

    db_user = get_user_by_id(db, user_id)

    if db_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return update_user(db, db_user, user)


def delete_user_service(
    db: Session,
    user_id: int,
):

    db_user = get_user_by_id(db, user_id)

    if db_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    delete_user(db, db_user)