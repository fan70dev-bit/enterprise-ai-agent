from app.agent.registry import TOOLS
from app.agent.serializer import serialize
from app.llm.summarizer import summarize


def execute(
    plan: dict,
    db,
    current_user,
):

    tool_name = plan["tool"]

    args = plan.get("args", {})

    tool = TOOLS.get(tool_name)

    if tool is None:
        return {
            "error": "Unknown tool"
        }

    result = tool(
        db=db,
        current_user=current_user,
        **args,
    )

    data = serialize(result)

    return summarize(data)