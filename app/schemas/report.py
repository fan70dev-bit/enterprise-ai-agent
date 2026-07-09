from datetime import datetime

from pydantic import BaseModel


class ReportCreate(BaseModel):
    content: str
    user_id: int


class ReportResponse(BaseModel):
    id: int
    user_id: int
    content: str
    created_at: datetime

    model_config = {
        "from_attributes": True,
    }