from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserCreate, UserResponse, LoginSchema, Token
from app.services.auth_service import register_user, login_user
from app.utils.response import success

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(data: UserCreate, db: Session = Depends(get_db)):
    user = register_user(data, db)
    return success(
        data={"id": user.id, "name": user.name, "email": user.email},
        message="User registered successfully"
    )

@router.post("/login", response_model=Token)
def login(data: LoginSchema, db: Session = Depends(get_db)):
    return login_user(data, db)