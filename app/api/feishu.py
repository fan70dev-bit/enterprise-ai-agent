import json

from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session

from app.db.database import SessionLocal, get_db

from app.core.deps import get_current_user

from app.models.user import User

from app.agent.agent import agent

from app.crud.user import get_user_by_open_id

from app.services.feishu import send_text_message
from app.crud.chat_message import create_message

from app.services.message_dedup import is_duplicate


router = APIRouter()


@router.post("/feishu/webhook")
async def webhook(request: Request):

    data = await request.json()

    print("=" * 60)
    print("Receive Event:")
    print(data)
    print("=" * 60)

    # 飞书 URL 验证
    if data.get("type") == "url_verification":
        return {
            "challenge": data["challenge"]
        }

    # 只处理消息事件
    if data["header"]["event_type"] != "im.message.receive_v1":
        return {
            "ok": True
        }

    event = data["event"]

    message_id = event["message"]["message_id"]

    if is_duplicate(message_id):
        print("Duplicate message detected.")
        return {
            "ok": True
        }

    chat_id = event["message"]["chat_id"]

    content = json.loads(
        event["message"]["content"]
    )

    text = content["text"]

    print("chat_id:", chat_id)
    print("text:", text)

    db: Session = SessionLocal()

    try:

        current_user = get_user_by_open_id(
            db,
            event["sender"]["sender_id"]["open_id"],
        )

        if current_user is None:

            print("User Not Bind.")

            return {
                "ok": True
            }
        
        create_message(
            db=db,
            user_id=current_user.id,
            role="user",
            content=text,
        )

        reply = agent.run(
            message=text,
            db=db,
            current_user=current_user,
        )

        send_text_message(
            chat_id=chat_id,
            text=str(reply),
        )

        print("=" * 60)
        print("Agent Reply:")
        print(reply)
        print("=" * 60)

        # 下一步将在这里调用飞书发送消息 API
        # send_message(chat_id, reply)

    except Exception as e:

        print(e)

    finally:

        db.close()

    return {
        "ok": True
    }


@router.post("/feishu/bind")
def bind_open_id(
    open_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    current_user.open_id = open_id

    db.commit()

    db.refresh(current_user)

    return {
        "message": "Bind Success",
        "open_id": current_user.open_id,
    }