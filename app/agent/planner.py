import json

from app.llm.client import llm


SYSTEM_PROMPT = """
你是企业办公AI Agent。

你的职责是分析用户请求，并决定需要调用哪些工具。

只能返回 JSON。

格式：

{
    "tools":[
        {
            "tool":"工具名",
            "args":{}
        }
    ]
}

支持工具：

get_my_tasks
get_my_reports
get_user_info
generate_report
chat

规则：

1. 普通聊天请选择 chat。
2. 查询任务请选择 get_my_tasks。
3. 查询日报请选择 get_my_reports。
4. 查询用户请选择 get_user_info。
5. 一个问题可以调用多个工具。

示例：

用户：
你好

返回：

{
    "tools":[
        {
            "tool":"chat",
            "args":{}
        }
    ]
}

用户：
查询我的任务

返回：

{
    "tools":[
        {
            "tool":"get_my_tasks",
            "args":{}
        }
    ]
}

不要输出 Markdown。
不要解释。
不要输出 ```json。
"""


def plan(
    message: str,
    history: list,
):

    # ======== 第一层：规则判断 ========

    if "任务" in message:
        return {
            "tools": [
                {
                    "tool": "get_my_tasks",
                    "args": {}
                }
            ]
        }

    if "日报" in message:
        return {
            "tools": [
                {
                    "tool": "get_my_reports",
                    "args": {}
                }
            ]
        }

    if (
        "部门" in message
        or "邮箱" in message
        or "用户信息" in message
        or "个人信息" in message
    ):
        return {
            "tools": [
                {
                    "tool": "get_user_info",
                    "args": {}
                }
            ]
        }

    # ======== 其它全部走聊天 ========

    return {
        "tools": [
            {
                "tool": "chat",
                "args": {}
            }
        ]
    }