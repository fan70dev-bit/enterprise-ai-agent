from app.agent.registry import TOOLS
from app.agent.serializer import serialize
from app.llm.summarizer import summarize


def execute(
    plan: dict,
    db,
    current_user,
    message: str,
):

    tools = plan.get("tools", [])

    if not tools:
        return "没有找到可以执行的工具。"

    # 保存所有 Tool 的结果
    context = {}

    for item in tools:

        tool_name = item["tool"]
        args = item.get("args", {})

        tool = TOOLS.get(tool_name)

        if tool is None:
            continue

        # 普通聊天
        if tool_name == "chat":
            return tool(
                db=db,
                current_user=current_user,
                message=message,
            )

        # 将之前 Tool 的结果传递给后续 Tool
        result = tool(
            db=db,
            current_user=current_user,
            context=context,
            **args,
        )

        context[tool_name] = serialize(result)

    # 如果只有一个 Tool，直接总结
    return summarize(
        message=message,
        data=context,
    )