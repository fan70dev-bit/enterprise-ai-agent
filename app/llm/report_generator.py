from app.llm.client import llm


SYSTEM_PROMPT = """
你是一名企业办公AI助手。

下面会给你今天完成的任务。

请生成一份专业、简洁的中文工作日报。

要求：

1. 使用自然语言。
2. 不要编造不存在的任务。
3. 100字左右即可。
4. 最后增加一句：
   明日计划：继续推进当前任务。
"""


def generate_daily_report(tasks):

    task_text = ""

    if not tasks:
        task_text = "今天没有完成任何任务。"

    else:

        for task in tasks:

            # 兼容 serialize() 后的 dict
            if isinstance(task, dict):

                title = task.get("title", "未知任务")
                status = task.get("status", "")
                priority = task.get("priority", "")

            else:

                title = task.title
                status = task.status
                priority = task.priority

            task_text += (
                f"- {title}"
                f"（状态：{status}，优先级：{priority}）\n"
            )

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        {
            "role": "user",
            "content": f"今日完成任务：\n\n{task_text}",
        },
    ]

    return llm.chat(messages)