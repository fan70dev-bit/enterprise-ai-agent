from fastapi import FastAPI

from app.api.department import router as department_router
from app.api.user import router as user_router
from app.api.auth import router as auth_router
from app.api.task import router as task_router

app = FastAPI(
    title="Enterprise AI Assistant",
    version="0.1.0",
)

app.include_router(auth_router)

app.include_router(department_router)
app.include_router(user_router)
app.include_router(task_router)

@app.get("/")
async def root():
    return {"message": "Enterprise AI Assistant is running!"}