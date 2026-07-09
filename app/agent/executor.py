from app.agent.registry import TOOLS


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

    return tool(
        db=db,
        current_user=current_user,
        **args,
    )