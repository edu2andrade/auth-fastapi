from datetime import datetime, timezone
from fastapi import APIRouter, HTTPException
from sqlmodel import select
from app.database import SessionDep
from app.models.user import User
from app.schemas.form import SignUp
from app.schemas.user import UserSession
from app.dependencies import create_access_token, create_refresh_token, validate_password
from app.repository.user import create_user

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/signup", response_model=UserSession, status_code=201)
async def signup(user_data: SignUp, db_session: SessionDep):
    # validate user data
    valid_password = validate_password(user_data.password)
    if not valid_password:
        raise HTTPException(status_code=400, detail="Password must contain at least 8 characters, 1 uppercase letter, 1 lowercase letter, 1 number, and 1 special character")

    # check if user already exists
    existing_user = db_session.exec(select(User).filter(User.email == user_data.email)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    # create new user in db
    new_user = create_user(user_data, db_session)
    if not new_user:
        raise HTTPException(status_code=400, detail="User not created")
    # create tokens
    access_token = create_access_token(str(new_user.id))
    refresh_token = create_refresh_token(str(new_user.id))

    # user response
    user_response = {
        "id": str(new_user.id),
        "username": user_data.username,
        "email": user_data.email,
        "created_at": datetime.now(timezone.utc),
        "updated_at": datetime.now(timezone.utc),
        "access_token": access_token,
        "refresh_token": refresh_token
    }
    # return user session
    return user_response