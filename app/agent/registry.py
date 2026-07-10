from app.agent.chat import chat

from app.agent.tools import (
    get_my_tasks,
    get_my_reports,
    get_user_info,
    create_task,
    update_task,
    delete_task,
)

TOOLS = {
    "chat": chat,

    "get_my_tasks": get_my_tasks,

    "get_my_reports": get_my_reports,

    "get_user_info": get_user_info,

    "create_task": create_task,

    "update_task": update_task,

    "delete_task": delete_task,
}