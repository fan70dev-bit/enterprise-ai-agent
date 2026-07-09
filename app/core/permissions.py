from fastapi import HTTPException
from app.models.user import User


def require_admin(
    user: User
):
    if user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin permission required"
        )

    return user