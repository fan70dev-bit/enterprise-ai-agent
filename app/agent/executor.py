import json
import time
import traceback


from app.agent.registry import TOOLS
from app.agent.serializer import serialize
from app.llm.summarizer import summarize

from app.crud.agent_log import create_agent_log



def execute(
    plan: dict,
    db,
    current_user,
    message: str,
):

    start_time = time.time()

    used_tools = []

    print("=" * 50)
    print("Planner Result:")
    print(plan)
    print("=" * 50)


    tools = plan.get("tools", [])


    if not tools:

        create_agent_log(
            db=db,
            data={
                "user_id": current_user.id,
                "message": message,
                "plan": json.dumps(
                    plan,
                    ensure_ascii=False,
                ),
                "tools": "[]",
                "latency": time.time()-start_time,
                "status": "failed",
                "error": "No tools found",
            },
        )

        return "没有找到可以执行的工具。"


    context = {}


    try:

        for item in tools:


            tool_name = item["tool"]

            args = item.get(
                "args",
                {}
            )


            tool = TOOLS.get(tool_name)


            if tool is None:
                continue


            used_tools.append(tool_name)


            # 普通聊天
            if tool_name == "chat":

                result = tool(
                    db=db,
                    current_user=current_user,
                    message=message,
                )

                create_agent_log(
                    db=db,
                    data={
                        "user_id": current_user.id,
                        "message": message,
                        "plan": json.dumps(
                            plan,
                            ensure_ascii=False,
                        ),
                        "tools": json.dumps(
                            used_tools,
                            ensure_ascii=False,
                        ),
                        "latency": time.time()-start_time,
                        "status": "success",
                    },
                )

                return result



            result = tool(
                db=db,
                current_user=current_user,
                context=context,
                **args,
            )


            context[tool_name] = serialize(result)



        reply = summarize(
            message=message,
            data=context,
        )


        create_agent_log(
            db=db,
            data={
                "user_id": current_user.id,
                "message": message,
                "plan": json.dumps(
                    plan,
                    ensure_ascii=False,
                ),
                "tools": json.dumps(
                    used_tools,
                    ensure_ascii=False,
                ),
                "latency": time.time()-start_time,
                "status": "success",
            },
        )


        return reply



    except Exception as e:


        traceback.print_exc()


        create_agent_log(
            db=db,
            data={
                "user_id": current_user.id,
                "message": message,
                "plan": json.dumps(
                    plan,
                    ensure_ascii=False,
                ),
                "tools": json.dumps(
                    used_tools,
                    ensure_ascii=False,
                ),
                "latency": time.time()-start_time,
                "status": "failed",
                "error": str(e),
            },
        )


        raise