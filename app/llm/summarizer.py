from app.llm.client import llm


SYSTEM_PROMPT = """
你是企业办公 AI 助手。

用户提出了一个问题。

系统已经调用了工具，并返回了真实数据。

请根据工具返回的数据回答用户。

要求：

1. 不要编造不存在的数据。
2. 回答自然、简洁。
3. 不要输出 JSON。
4. 不要解释推理过程。
5. 回答控制在 200 字以内。
"""


def summarize(
    message: str,
    data,
):
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        {
            "role": "user",
            "content": f"""
用户问题：

{message}

工具返回的数据：

{data}
""",
        },
    ]

    return llm.chat(messages)