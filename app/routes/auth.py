from fastapi import APIRouter, HTTPException
from app.models.form import SignUpForm, SignUpResponse
from uuid import uuid4
from datetime import datetime

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/signup", response_model=SignUpResponse, status_code=201)
async def signup(user_data: SignUpForm):
    # check if user already exists
    # validate user data
    # hash password
    # create new user in db
    # create access token
    user_response = {
        "id": uuid4(),
        "username": user_data.username,
        "email": user_data.email,
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "access_token": "token"
    }
    return user_response