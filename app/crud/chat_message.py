from sqlalchemy.orm import Session

from app.models.chat_message import ChatMessage


def create_message(
    db: Session,
    user_id: int,
    role: str,
    content: str,
):

    message = ChatMessage(
        user_id=user_id,
        role=role,
        content=content,
    )

    db.add(message)
    db.commit()
    db.refresh(message)

    return message


def list_messages(
    db: Session,
    user_id: int,
    limit: int = 20,
):

    return (
        db.query(ChatMessage)
        .filter(ChatMessage.user_id == user_id)
        .order_by(ChatMessage.id.desc())
        .limit(limit)
        .all()[::-1]
    )