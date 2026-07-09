from app.agent.planner import plan
from app.agent.executor import execute


class EnterpriseAgent:

    def run(
        self,
        message: str,
        db,
        current_user,
    ):

        action = plan(message)

        print("=" * 50)
        print("Planner Result:")
        print(action)
        print("=" * 50)

        return execute(
            plan=action,
            db=db,
            current_user=current_user,
        )


agent = EnterpriseAgent()