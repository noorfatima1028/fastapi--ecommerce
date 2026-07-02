from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate
from fastapi import HTTPException

def get_all_products(db: Session):
    return db.query(Product).filter(Product.is_active == True).all()

def get_product(id: int, db: Session):
    product = db.query(Product).filter(Product.id == id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

def create_product(data: ProductCreate, db: Session):
    product = Product(**data.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def update_product(id: int, data: ProductUpdate, db: Session):
    product = get_product(id, db)
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product

def delete_product(id: int, db: Session):
    product = get_product(id, db)
    product.is_active = False
    db.commit()
    return {"message": "Product deleted"}