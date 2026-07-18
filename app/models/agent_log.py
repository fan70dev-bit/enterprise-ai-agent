from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    Text,
    Float,
    DateTime,
    String,
)
from app.db.base import Base


class AgentLog(Base):

    __tablename__ = "agent_logs"


    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )


    user_id = Column(
        Integer,
        nullable=False,
    )


    message = Column(
        Text,
        nullable=False,
    )


    plan = Column(
        Text,
        nullable=True,
    )


    tools = Column(
        Text,
        nullable=True,
    )


    latency = Column(
        Float,
        nullable=True,
    )


    status = Column(
        String(20),
        default="success",
    )


    error = Column(
        Text,
        nullable=True,
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )