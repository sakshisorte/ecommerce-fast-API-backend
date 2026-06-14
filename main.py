from fastapi import FastAPI

from database import Base, engine
from routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-Commerce Backend API")

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "E-Commerce Backend Running Successfully"
    }