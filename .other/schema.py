from typing import Union

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):# This the schema
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.post("/createposts")
def create_posts(post: Post):
    print(post)
    print(post.model_dump())
    return post.model_dump()
    

