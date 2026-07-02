from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.cart import CartItemAdd, CartResponse
from app.services.cart_service import add_to_cart, remove_from_cart, view_cart
from app.utils.jwt import get_current_user
from app.models.user import User

router = APIRouter(prefix="/cart", tags=["Cart"])

@router.get("/", response_model=CartResponse)
def get_cart(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return view_cart(user, db)

@router.post("/", response_model=CartResponse)
def add_item(data: CartItemAdd, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return add_to_cart(data, user, db)

@router.delete("/{product_id}")
def remove_item(product_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return remove_from_cart(product_id, user, db)