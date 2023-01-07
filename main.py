from fastapi import FastAPI, Request
from tinydb import TinyDB

from utils import type_form, is_correct_form, convert_qs_to_dict

app = FastAPI()
db = TinyDB("db.json")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/get_form/")
async def get_form(request: Request):
    body = (await request.body()).decode("utf-8")
    data = convert_qs_to_dict(body)
    form = type_form(data)
    for item in db:
        if is_correct_form(form, item):
            return item["name"]
    return form
