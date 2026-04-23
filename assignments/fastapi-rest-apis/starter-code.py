from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Mergington FastAPI Assignment")


class Item(BaseModel):
    name: str
    price: float
    in_stock: bool


items = [
    {"name": "Notebook", "price": 4.99, "in_stock": True},
    {"name": "Pen", "price": 1.5, "in_stock": True},
    {"name": "Backpack", "price": 29.99, "in_stock": False},
]


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/items")
def get_items():
    return items


@app.post("/items")
def create_item(item: Item):
    new_item = item.model_dump()
    items.append(new_item)
    return new_item
