from app.agent.planner import plan
from app.agent.executor import execute

from app.memory.memory import get_messages


class EnterpriseAgent:

    def run(
        self,
        message: str,
        db,
        current_user,
    ):

        # 获取历史聊天
        history = get_messages(
            db=db,
            user_id=current_user.id,
        )

        # Planner 决策
        action = plan(
            message=message,
            history=history,
        )

        print("=" * 50)
        print("Planner Result:")
        print(action)
        print("=" * 50)

        # 执行工具
        return execute(
            plan=action,
            db=db,
            current_user=current_user,
            message=message,
        )


agent = EnterpriseAgent()