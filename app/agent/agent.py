from app.agent.history import build_history
from app.agent.planner import plan
from app.agent.executor import execute


class EnterpriseAgent:

    def run(
        self,
        message: str,
        db,
        current_user,
    ):

        history = build_history(
            db=db,
            current_user=current_user,
        )

        action = plan(
            message=message,
            history=history,
        )

        return execute(
            plan=action,
            db=db,
            current_user=current_user,
            message=message,
        )


agent = EnterpriseAgent()