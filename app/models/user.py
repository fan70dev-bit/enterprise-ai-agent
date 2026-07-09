from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class User(Base):

    __tablename__ = "users"


    id: Mapped[int] = mapped_column(
        primary_key=True
    )


    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )


    email: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )


    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )


    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )


    role: Mapped[str] = mapped_column(
        String(20),
        default="employee"
    )


    department_id: Mapped[int] = mapped_column(
        ForeignKey("department.id"),
        nullable=False
    )


    department = relationship(
        "Department",
        back_populates="users"
    )