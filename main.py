import uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

@app.get("/blog")
def index(limit=10 ,published:bool=True , sort:Optional[str]=None):

    if published:
        return {'data':f'{limit} published blog from the db'}
    else:
        return {'data':f'{limit} blog from the db'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@app.get("/about")
def about():
    return {'data':'about page'}

@app.get("/blog/{id}")
def show(id:int):
    return {'data': id}

@app.get("/blog/{id}/comments")
def comments(id:str):
    """ test"""
    return {'data':{'1', '2'}}

class Blog(BaseModel):
    tittle:str
    body:str
    published_at:Optional[bool]


@app.post('/blog')
def create_blog(blog:Blog):
    return {f'data':'blog is created with tittle at {blog.tittle}'}





