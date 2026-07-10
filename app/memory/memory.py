from sqlalchemy.orm import Session

from app.models.chat_message import ChatMessage


def add_message(
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


def get_messages(
    db: Session,
    user_id: int,
    limit: int = 20,
):

    messages = (
        db.query(ChatMessage)
        .filter(ChatMessage.user_id == user_id)
        .order_by(ChatMessage.id.desc())
        .limit(limit)
        .all()
    )

    messages.reverse()

    return [
        {
            "role": m.role,
            "content": m.content,
        }
        for m in messages
    ]