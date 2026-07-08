from fastapi import FastAPI

from app.api.department import router as department_router

app = FastAPI(
    title="Enterprise AI Assistant",
    version="0.1.0",
)

app.include_router(department_router)

@app.get("/")
async def root():
    return {"message": "Enterprise AI Assistant is running!"}