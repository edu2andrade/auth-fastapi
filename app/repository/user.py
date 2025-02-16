from uuid import uuid4
from datetime import datetime, timezone
from sqlmodel import Session
from app.schemas.form import SignUp
from app.models.user import User
from app.dependencies import hash_password

def create_user(user_data: SignUp, db_session: Session):
    new_user = User(
        id=uuid4(),
        username=user_data.username,
        email=user_data.email,
        password_hash=hash_password(user_data.password),
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc)
    )

    db_session.add(new_user)
    db_session.commit()
    db_session.refresh(new_user)
    
    return new_user