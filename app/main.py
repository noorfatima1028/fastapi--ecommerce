from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import SQLAlchemyError
from app.database import Base, engine
from app.routers import auth, products, cart, orders

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI E-Commerce",
    description="A full e-commerce REST API built with FastAPI",
    version="1.0"
)

# Handle validation errors
@app.exception_handler(RequestValidationError)
async def validation_error_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": "Invalid input", "errors": exc.errors()}
    )

# Handle database errors
@app.exception_handler(SQLAlchemyError)
async def db_error_handler(request: Request, exc: SQLAlchemyError):
    return JSONResponse(
        status_code=500,
        content={"detail": "Database error occurred"}
    )

app.include_router(auth.router)
app.include_router(products.router)
app.include_router(cart.router)
app.include_router(orders.router)

@app.get("/", tags=["Root"])
def root():
    return {"message": "E-Commerce API is running 🚀", "docs": "/docs"}