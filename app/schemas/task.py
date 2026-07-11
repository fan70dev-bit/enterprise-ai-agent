from datetime import datetime

from pydantic import BaseModel


class TaskBase(BaseModel):

    title: str

    description: str | None = None

    status: str = "todo"

    priority: str = "medium"

    user_id: int | None = None



class TaskCreate(TaskBase):
    pass



class TaskUpdate(BaseModel):

    title: str | None = None

    description: str | None = None

    status: str | None = None

    priority: str | None = None

    user_id: int | None = None



class TaskResponse(TaskBase):

    id: int

    created_at: datetime


    class Config:
        from_attributes = True