from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.core.deps import get_current_user

from app.models.user import User

from app.agent.agent import agent


router = APIRouter(
    prefix="/agent",
    tags=["Agent"],
)


@router.post("/chat")
def chat(
    message: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    result = agent.run(
        message=message,
        db=db,
        current_user=current_user,
    )

    return result