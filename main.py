from fastapi import FastAPI, Request
from tinydb import TinyDB

from utils import predicate, type_form

app = FastAPI()
db = TinyDB("db.json")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/get_form/")
async def get_form(request: Request):
    body = await request.json()
    form_from_request = type_form(body)
    form_from_db = db.search(lambda obj: predicate(obj, form_from_request))
    if form_from_db:
        return form_from_db[0]["name"]
    return form_from_request
