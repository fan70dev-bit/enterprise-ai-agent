from app.agent.registry import TOOLS
from app.agent.serializer import serialize
from app.llm.summarizer import summarize


def execute(
    plan: dict,
    db,
    current_user,
):

    results = {}

    tools = plan.get("tools", [])

    if not tools:
        return "没有找到可以执行的工具。"

    for item in tools:

        tool_name = item["tool"]

        args = item.get("args", {})

        tool = TOOLS.get(tool_name)

        if tool is None:
            continue

        result = tool(
            db=db,
            current_user=current_user,
            **args,
        )

        results[tool_name] = serialize(result)

    return summarize(results)