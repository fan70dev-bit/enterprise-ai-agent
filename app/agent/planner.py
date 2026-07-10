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

chat
get_my_tasks
get_my_reports
get_user_info
create_task
update_task
delete_task
generate_report

规则：

1. 普通聊天请选择 chat。
2. 查询任务请选择 get_my_tasks。
3. 查询日报请选择 get_my_reports。
4. 查询用户请选择 get_user_info。
5. 创建任务请选择 create_task。
6. 修改任务请选择 update_task。
7. 删除任务请选择 delete_task。
8. 一个问题可以调用多个工具。
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

用户：

帮我创建一个高优先级任务

标题：完成周报

描述：整理本周工作

返回：

{
    "tools":[
        {
            "tool":"create_task",
            "args":{
                "title":"完成周报",
                "description":"整理本周工作",
                "priority":"high"
            }
        }
    ]
}

用户：

把完成周报改成已完成

返回：

{
    "tools":[
        {
            "tool":"update_task",
            "args":{
                "title":"完成周报",
                "status":"done"
            }
        }
    ]
}

用户：

删除完成周报

返回：

{
    "tools":[
        {
            "tool":"delete_task",
            "args":{
                "title":"完成周报"
            }
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

    # ========= 第一层：快速规则 =========

    if (
        "查询任务" in message
        or "我的任务" in message
        or "任务列表" in message
    ):
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

    # ========= 第二层：LLM Planner =========

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

    result = llm.chat(messages)

    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    try:
        return json.loads(result)

    except Exception:

        return {
            "tools": [
                {
                    "tool": "chat",
                    "args": {}
                }
            ]
        }