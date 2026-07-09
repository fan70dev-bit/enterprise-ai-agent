from app.llm.client import llm


def generate_report(tasks: list):

    if not tasks:
        return "今天暂无任务。"

    task_text = ""

    for i, task in enumerate(tasks, start=1):
        task_text += (
            f"{i}. {task.title}"
            f"\n描述：{task.description}"
            f"\n状态：{task.status}\n\n"
        )

    messages = [
        {
            "role": "system",
            "content": (
                "你是一名企业员工，"
                "请根据今天完成的任务生成一份正式日报。"
            ),
        },
        {
            "role": "user",
            "content": (
                f"""
今天完成的任务：

{task_text}

请输出：

今日完成：
工作总结：
明日计划：

控制在200字以内。
"""
            ),
        },
    ]

    return llm.chat(messages)