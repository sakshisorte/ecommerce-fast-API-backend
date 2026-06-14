from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float


class OrderCreate(BaseModel):
    user_id: int
    product_id: int