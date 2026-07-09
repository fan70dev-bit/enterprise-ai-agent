from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.core.deps import get_current_user
from app.models.user import User

from app.crud.task import list_tasks_by_user

from app.agent.report_generator import generate_report

router = APIRouter(
    prefix="/agent",
    tags=["Agent"],
)


@router.post("/report")
def generate_daily_report(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    tasks = list_tasks_by_user(
        db,
        current_user.id,
    )

    report = generate_report(tasks)

    return {
        "report": report,
    }