from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    department_id: int


class UserUpdate(BaseModel):
    username: str
    email: str
    department_id: int


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool
    department_id: int

    class Config:
        from_attributes = True