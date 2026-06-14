from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models
import schemas

from database import SessionLocal
from auth import hash_password

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(
        username=user.username,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()

    return {"message": "User Registered Successfully"}


@router.post("/products")
def add_product(product: schemas.ProductCreate,
                db: Session = Depends(get_db)):
    new_product = models.Product(
        name=product.name,
        description=product.description,
        price=product.price
    )

    db.add(new_product)
    db.commit()

    return {"message": "Product Added Successfully"}


@router.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()


@router.post("/orders")
def place_order(order: schemas.OrderCreate,
                db: Session = Depends(get_db)):
    new_order = models.Order(
        user_id=order.user_id,
        product_id=order.product_id
    )

    db.add(new_order)
    db.commit()

    return {"message": "Order Placed Successfully"}


@router.get("/orders")
def get_orders(db: Session = Depends(get_db)):
    return db.query(models.Order).all()