from app.agent.tools import (
    get_my_tasks,
    get_my_reports,
    get_user_info,
)

from app.agent.chat import chat


TOOLS = {
    "chat": chat,

    "get_my_tasks": get_my_tasks,

    "get_my_reports": get_my_reports,

    "get_user_info": get_user_info,
}