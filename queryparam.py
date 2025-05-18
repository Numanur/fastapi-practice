from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
'''FastAPI automatically treats skip and limit as query parameters. Query parameters are the key-value pairs that appear after the ? in a URL. /items/?skip=5&limit=10
In FastAPI:
If a function parameter is not part of the path, and
It has a default value (like skip: int = 0)
Then FastAPI automatically interprets it as a query parameter.'''

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

'''In this case, item_id is a path parameter, and q is a query parameter. The q parameter is optional and can be None. If q is provided in the URL, it will be included in the response. If not, it will not be included.'''

@app.get("/itemss/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
'''In this case, item_id is a path parameter, q is an optional query parameter, and short is a boolean query parameter. If short is set to True, the response will not include the long description. If it is set to False or not provided, the long description will be included.'''