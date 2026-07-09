from datetime import datetime

from sqlalchemy import Text, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Report(Base):

    __tablename__ = "reports"


    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )


    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )


    content: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now
    )


    user = relationship(
        "User",
        back_populates="reports"
    )