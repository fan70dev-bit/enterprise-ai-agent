from app.llm.client import llm


def summarize(data):

    messages = [
        {
            "role": "system",
            "content": """
你是企业办公AI。

请根据提供的数据，
生成自然、简洁的中文回答。

不要输出JSON。

不要解释你的推理。

回答控制在200字以内。
""",
        },
        {
            "role": "user",
            "content": str(data),
        },
    ]

    return llm.chat(messages)