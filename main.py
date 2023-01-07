from fastapi import FastAPI, Request
from tinydb import TinyDB, Query

app = FastAPI()
db = TinyDB("db.json")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/get_form/")
async def get_form(request: Request):
    body = await request.body()
    print(body)
    for item in db:
        print(item)
    return await request.json()
