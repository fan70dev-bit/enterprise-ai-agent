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

    results = {}

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

        # 业务工具
        result = tool(
            db=db,
            current_user=current_user,
            **args,
        )

        results[tool_name] = serialize(result)

    # 将多个 Tool 结果交给 LLM 总结
    return summarize(results)