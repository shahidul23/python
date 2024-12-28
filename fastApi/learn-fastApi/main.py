from fastapi import FastAPI
from enum import Enum
from typing import Optional

from fastapi.params import Query
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}



class FootItemsEnum(str, Enum):
    Fruits = "fruits"
    Vegetables = "vegetables"
    Dairy = "dairy"

@app.get("/foods/{food_name}")
async def get_food_items(food_name: FootItemsEnum):
    if food_name == FootItemsEnum.Vegetables:
        return {
            "food_name": food_name,
            "message": "You are healthy",
        }
    elif food_name == FootItemsEnum.Fruits:
        return {
            "food_name": food_name,
            "message": "You are healthy",
        }
    else:  # Default for Dairy
        return {
            "food_name": food_name,
            "message": "Dairy Chocolate",
        }

@app.get("/items")
async def read_items():
    return {
        "message": "get all items",
    }

fack_items_db =[
    {"item_name" : "foo"},{"item_name" : "fruits"},{"item_name" : "vegetables"},

]
@app.get("/item")
async def list_items(skip: int = 0, limit: int = 10):
    return fack_items_db[skip : skip + limit]

@app.get("/item/{item_id}")
async def get_items(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "this is a short description"})
    return item

@app.get("/users/{user_id}/items/{item_id}")
async def get_users_items(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "Owner_id" : user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "this is a short description"})
    return item


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: float | None = None

@app.post("/items")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.put("/items/{item_id}")
async def create_item_with_put(item_id: int, item: Item, q: str | None = None):
    result =  {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


# @app.get("/itemsget")
# async def read_items(q: str | None = Query(None, min_length=3, max_length=10, regex=r"^[a-zA-Z]+$")):
#     result = {"items":[{"item_id": "foo"}, {"item_id": "fruits"}, {"item_id": "vegetables"}]}
#     if q:
#         result.update({"q": q})
#     return result

# @app.get("/itemsget")
# async def read_items(q: list[str] = Query(["foo", "bar"])):
#     result = {"items":[{"item_id": "foo"}, {"item_id": "fruits"}, {"item_id": "vegetables"}]}
#     if q:
#         result.update({"q": q})
#     return result

@app.get("/itemsquery")
async def get_items_query(
    items_query: str
    | None = Query(
    None,
    min_length=3,
    max_length=10,
    title="Sample Query string",
    description="Sample Query string",
    alias="sample",
    )
):
    result = {"items": [{"item_id" : "foo"}, {"item_id" : "fruits"}, {"item_id" : "vegetables"}] }
    if items_query:
        result.update({"q": items_query})
    return result

@app.get("/items/hidden")
async def get_items_hidden_query(hidden_query: str | None = Query(None, include_in_schema=False)):
    if hidden_query:
        return {"hidden_query": hidden_query}
    return {"hidden_query": "Not found"}
