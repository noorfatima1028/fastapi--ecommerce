from fastapi import FastAPI
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI E-Commerce", version="1.0")

@app.get("/")
def root():
    return {"message": "E-Commerce API is running 🚀"}