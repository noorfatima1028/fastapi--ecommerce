from sqlalchemy.orm import Session
from app.models.cart import Cart, CartItem
from app.models.user import User
from app.schemas.cart import CartItemAdd
from fastapi import HTTPException

def get_or_create_cart(user: User, db: Session):
    cart = db.query(Cart).filter(Cart.user_id == user.id).first()
    if not cart:
        cart = Cart(user_id=user.id)
        db.add(cart)
        db.commit()
        db.refresh(cart)
    return cart

def add_to_cart(data: CartItemAdd, user: User, db: Session):
    cart = get_or_create_cart(user, db)
    item = db.query(CartItem).filter(
        CartItem.cart_id == cart.id,
        CartItem.product_id == data.product_id
    ).first()
    if item:
        item.quantity += data.quantity
    else:
        item = CartItem(cart_id=cart.id, product_id=data.product_id, quantity=data.quantity)
        db.add(item)
    db.commit()
    db.refresh(cart)
    return cart

def remove_from_cart(product_id: int, user: User, db: Session):
    cart = get_or_create_cart(user, db)
    item = db.query(CartItem).filter(
        CartItem.cart_id == cart.id,
        CartItem.product_id == product_id
    ).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not in cart")
    db.delete(item)
    db.commit()
    return {"message": "Item removed"}

def view_cart(user: User, db: Session):
    return get_or_create_cart(user, db)