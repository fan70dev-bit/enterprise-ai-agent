import json

from app.llm.client import llm


SYSTEM_PROMPT = """
你是企业办公AI Agent。

请根据用户请求选择最合适的工具。

只能返回 JSON。

格式如下：

{
    "tool":"工具名",
    "args":{}
}

目前支持：

get_my_tasks
get_my_reports
get_user_info
generate_report

如果没有对应工具：

{
    "tool":"chat",
    "args":{}
}

不要输出 Markdown。
不要解释。
不要输出 ```json。
"""


def plan(message: str):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        {
            "role": "user",
            "content": message,
        },
    ]

    result = llm.chat(messages)

    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    return json.loads(result)