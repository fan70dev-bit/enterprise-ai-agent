from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.auth import TokenResponse

from app.crud.user import get_user_by_username
from app.core.security import (
    verify_password,
    create_access_token,
)

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):

    user = get_user_by_username(
        db,
        form_data.username,
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="用户名或密码错误",
        )

    if not verify_password(
        form_data.password,
        user.hashed_password,
    ):
        raise HTTPException(
            status_code=401,
            detail="用户名或密码错误",
        )

    token = create_access_token(
        {
            "sub": str(user.id),
            "username": user.username,
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }