from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    passwd: str
    is_active: bool
    is_superuser: bool

class UserUpdate(BaseModel):
    id: int
    username: str
    email: str
    passwd: str
    is_active: bool
    is_superuser: bool

class UserSelect(BaseModel):
    username: str
    email: str
    is_active: bool
    is_superuser: bool