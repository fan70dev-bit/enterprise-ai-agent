from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

from app.core.security import get_password_hash


def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=get_password_hash(user.password),
        department_id=user.department_id,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user_by_id(db: Session, user_id: int) -> User | None:
    return (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )


def get_user_by_username(db: Session, username: str) -> User | None:
    return (
        db.query(User)
        .filter(User.username == username)
        .first()
    )


def list_users(db: Session) -> list[User]:
    return db.query(User).all()


def update_user(
    db: Session,
    db_user: User,
    user: UserUpdate,
) -> User:

    db_user.username = user.username
    db_user.email = user.email
    db_user.department_id = user.department_id

    db.commit()
    db.refresh(db_user)

    return db_user


def delete_user(
    db: Session,
    db_user: User,
) -> None:

    db.delete(db_user)
    db.commit()


def get_user_by_open_id(
    db: Session,
    open_id: str,
) -> User | None:

    return (
        db.query(User)
        .filter(User.open_id == open_id)
        .first()
    )