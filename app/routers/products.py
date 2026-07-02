from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse
from app.services.product_service import (
    get_all_products, get_product,
    create_product, update_product, delete_product
)
from typing import List

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=List[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return get_all_products(db)

@router.get("/{id}", response_model=ProductResponse)
def single_product(id: int, db: Session = Depends(get_db)):
    return get_product(id, db)

@router.post("/", response_model=ProductResponse)
def add_product(data: ProductCreate, db: Session = Depends(get_db)):
    return create_product(data, db)

@router.put("/{id}", response_model=ProductResponse)
def edit_product(id: int, data: ProductUpdate, db: Session = Depends(get_db)):
    return update_product(id, data, db)

@router.delete("/{id}")
def remove_product(id: int, db: Session = Depends(get_db)):
    return delete_product(id, db)