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

