from fastapi import FastAPI
from . import scehmas

app=FastAPI()


@app.post("/blog")
def create(request: scehmas.Blog):
    return request