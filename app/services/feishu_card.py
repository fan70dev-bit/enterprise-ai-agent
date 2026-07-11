import json
import requests

from app.services.feishu import get_tenant_access_token


def send_task_card(
    chat_id: str,
    tasks: list,
):
    """
    发送任务卡片
    """

    token = get_tenant_access_token()

    url = "https://open.feishu.cn/open-apis/im/v1/messages"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    elements = []

    if not tasks:

        elements.append(
            {
                "tag": "markdown",
                "content": "暂无任务 🎉"
            }
        )

    else:

        for task in tasks:

            status = "🟢 已完成" if task["status"] == "done" else "🔴 待办"

            priority = {
                "high": "高",
                "medium": "中",
                "low": "低",
            }.get(task["priority"], task["priority"])

            elements.append(
                {
                    "tag": "markdown",
                    "content":
                        f"**{task['title']}**\n"
                        f"{status}\n"
                        f"优先级：{priority}"
                }
            )

            elements.append(
                {
                    "tag": "hr"
                }
            )

    card = {
        "config": {
            "wide_screen_mode": True
        },
        "header": {
            "title": {
                "tag": "plain_text",
                "content": "📋 我的任务"
            }
        },
        "elements": elements
    }

    body = {
        "receive_id": chat_id,
        "msg_type": "interactive",
        "content": json.dumps(card, ensure_ascii=False),
    }

    resp = requests.post(
        url,
        headers=headers,
        params={
            "receive_id_type": "chat_id"
        },
        json=body,
        timeout=10,
    )

    print("=" * 60)
    print("Card Response:")
    print(resp.json())
    print("=" * 60)