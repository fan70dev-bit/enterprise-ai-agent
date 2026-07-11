from app.services.redis import redis_client


def is_duplicate(message_id: str) -> bool:
    """
    判断消息是否重复
    """

    key = f"message:{message_id}"

    success = redis_client.set(
        key,
        "1",
        nx=True,
        ex=600,
    )

    return success is None