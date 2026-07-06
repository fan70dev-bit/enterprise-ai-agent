from fastapi import FastAPI

app = FastAPI(
    title="Enterprise AI Assistant",
    version="0.1.0",
)

@app.get("/")
async def root():
    return {"message": "Enterprise AI Assistant is running!"}