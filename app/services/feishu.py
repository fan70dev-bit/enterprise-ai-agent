import json
import requests

from app.core.config import settings


def get_tenant_access_token():

    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"

    resp = requests.post(
        url,
        json={
            "app_id": settings.FEISHU_APP_ID,
            "app_secret": settings.FEISHU_APP_SECRET,
        },
        timeout=10,
    )

    resp.raise_for_status()

    data = resp.json()

    print("Tenant Token:", data)

    return data["tenant_access_token"]


def send_text_message(
    chat_id: str,
    text: str,
):

    token = get_tenant_access_token()

    url = "https://open.feishu.cn/open-apis/im/v1/messages"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    body = {
        "receive_id": chat_id,
        "msg_type": "text",
        "content": json.dumps(
            {
                "text": text
            },
            ensure_ascii=False,
        ),
    }

    print("=" * 60)
    print("Send Body:")
    print(body)
    print("=" * 60)

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
    print("Feishu Response:")
    print(resp.json())
    print("=" * 60)