from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.order import OrderResponse
from app.services.order_service import place_order, get_my_orders, get_order, update_order_status
from app.utils.jwt import get_current_user
from app.models.user import User
from typing import List

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/", response_model=OrderResponse)
def create_order(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return place_order(user, db)

@router.get("/", response_model=List[OrderResponse])
def my_orders(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return get_my_orders(user, db)

@router.get("/{order_id}", response_model=OrderResponse)
def single_order(order_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return get_order(order_id, user, db)

@router.patch("/{order_id}/status")
def change_status(order_id: int, status: str, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return update_order_status(order_id, status, db)