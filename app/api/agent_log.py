from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import json

from app.db.database import get_db
from app.models.agent_log import AgentLog


router = APIRouter(
    prefix="/agent",
    tags=["Agent Monitor"]
)


@router.get("/logs")
def get_logs(
    db: Session = Depends(get_db)
):

    logs = (
        db.query(AgentLog)
        .order_by(
            AgentLog.id.desc()
        )
        .limit(50)
        .all()
    )


    result = []

    for log in logs:

        result.append(
            {
                "id": log.id,
                "user_id": log.user_id,
                "message": log.message,
                "tools": json.loads(log.tools),
                "status": log.status,
                "latency": log.latency,
                "created_at": log.created_at,
                "error": log.error,
            }
        )


    return result