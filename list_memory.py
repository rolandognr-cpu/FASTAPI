from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):# This the schema
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [
            {"title": "Title of post 1", "content": "Content of post1", "id": 1},
            {"title": "Title of post 2", "content": "Content of post 2", "id": 2},
            {"title": "Title of post 3", "content": "Content of post 3", "id": 3},
            {"title": "Title of post 4", "content": "Content of post 4", "id": 4}
            ]

def find_post(arr, id):
    for p in arr:
        if p['id'] == id:
            return p
        
def find_post_index(arr, id):
    for i, p in enumerate(arr):
        if p['id'] == id:
            return i


@app.get("/posts")
def get_posts():
    return my_posts


@app.post("/posts", status_code=status.HTTP_201_CREATED )
def create_posts(post: Post):
    my_posts.append(post.model_dump())
    my_posts[-1]['id'] = len(my_posts)
    return my_posts
    
    

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(my_posts, id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} not found")
    
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"Post with id: {id} not found"}

    return post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_post_index(my_posts, id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} not found")
    
    my_posts.pop(index)
    return {"message": f"Post id: {id} was deleted"}

@app.put("/posts/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_post(id: int, post: Post):
    index = find_post_index(my_posts, id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} not found")
    my_posts[index] = post.model_dump()
    my_posts[index]['id'] = id
    return my_posts