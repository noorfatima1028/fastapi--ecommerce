from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth, products, cart, orders

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI E-Commerce", version="1.0")

app.include_router(auth.router)
app.include_router(products.router)
app.include_router(cart.router)
app.include_router(orders.router)

@app.get("/")
def root():
    return {"message": "E-Commerce API is running 🚀"}