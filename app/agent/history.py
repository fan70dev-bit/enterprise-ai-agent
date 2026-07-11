from app.crud.chat_message import list_messages


def build_history(
    db,
    current_user,
):
    """
    构建 LLM 上下文
    """

    history = []

    messages = list_messages(
        db=db,
        user_id=current_user.id,
        limit=20,
    )

    for message in messages:
        history.append(
            {
                "role": message.role,
                "content": message.content,
            }
        )

    return history