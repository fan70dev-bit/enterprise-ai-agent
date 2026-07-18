from fastapi import FastAPI

from app.api.feishu import router as feishu_router

from app.api.department import router as department_router
from app.api.user import router as user_router
from app.api.auth import router as auth_router
from app.api.task import router as task_router
from app.api.agent import router as agent_router
from app.api.agent_report import router as agent_report_router
from app.api.agent_log import router as agent_log_router
from app.api.report import router as report_router


app = FastAPI(
    title="Enterprise AI Assistant",
    version="0.1.0",
)


# Auth
app.include_router(auth_router)


# Business Modules
app.include_router(department_router)
app.include_router(user_router)
app.include_router(task_router)
app.include_router(report_router)

# Agent
app.include_router(agent_router)
app.include_router(agent_report_router)

# Feishu
app.include_router(feishu_router)

# Log
app.include_router(
    agent_log_router
)


@app.get("/")
async def root():
    return {
        "message": "Enterprise AI Assistant is running!"
    }