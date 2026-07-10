from sqlalchemy.orm import Session

from app.llm.client import llm

from app.memory.memory import (
    add_message,
    get_messages,
)


SYSTEM_PROMPT = """
你是一名企业AI办公助手。

请结合历史聊天回答用户问题。

如果用户告诉了你一些信息，请记住它。

回答要简洁自然。
"""


def chat(
    db: Session,
    current_user,
    message: str,
):
    """
    普通聊天
    """

    # 读取数据库历史消息
    history = get_messages(
        db=db,
        user_id=current_user.id,
    )

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        }
    ]

    messages.extend(history)

    messages.append(
        {
            "role": "user",
            "content": message,
        }
    )

    # 调用大模型
    result = llm.chat(messages)

    # 保存用户消息
    add_message(
        db=db,
        user_id=current_user.id,
        role="user",
        content=message,
    )

    # 保存AI回复
    add_message(
        db=db,
        user_id=current_user.id,
        role="assistant",
        content=result,
    )

    return result

def summarize_tool_result(
    message: str,
    tool_result,
):
    messages = [
        {
            "role": "system",
            "content": """
你是企业办公 AI 助手。

下面是工具返回的数据。

请根据数据回答用户。

不要编造。
回答简洁自然。
""",
        },
        {
            "role": "user",
            "content": f"""
用户问题：

{message}

工具结果：

{tool_result}
""",
        },
    ]

    return llm.chat(messages)