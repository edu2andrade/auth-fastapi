from uuid import UUID
from datetime import datetime
from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    id: UUID = Field(default=None, primary_key=True)
    username: str | None = Field(default=None)
    email: str
    password_hash: str
    access_token: str | None = Field(default=None)
    refresh_token: str | None = Field(default=None)
    created_at: datetime
    updated_at: datetime
