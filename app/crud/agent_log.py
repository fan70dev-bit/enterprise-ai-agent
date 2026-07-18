from sqlalchemy.orm import Session

from app.models.agent_log import AgentLog


def create_agent_log(
    db: Session,
    data: dict,
):

    log = AgentLog(
        **data
    )

    db.add(log)

    db.commit()

    db.refresh(log)

    return log