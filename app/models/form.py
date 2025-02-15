from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class SignUpForm(BaseModel):
    username: str
    email: EmailStr
    password: str

class SignUpResponse(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime
    access_token: str