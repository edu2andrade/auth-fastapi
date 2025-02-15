from uuid import UUID
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserSession(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    password_hash: str
    created_at: datetime
    updated_at: datetime
    