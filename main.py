from fastapi import FastAPI, Request
from tinydb import TinyDB

from utils import type_form, is_correct_form

app = FastAPI()
db = TinyDB("db.json")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/get_form/")
async def get_form(request: Request):
    body = await request.json()
    form = type_form(body)
    for item in db:
        if is_correct_form(item, form):
            return item["name"]
    return await request.json()
