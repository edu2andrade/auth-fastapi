from pydantic import BaseModel, EmailStr

class SignUp(BaseModel):
    username: str
    email: EmailStr
    password: str
