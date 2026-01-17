
from fastapi import FastAPI, status, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db
from .schemas import PostCreate, PostUpdtae

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Retrieve all posts
@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return{"data": posts}

# Retrieve posts by id
@app.get("/posts/{id}")
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found")
    return post

# Create a post
@app.post("/posts", status_code=status.HTTP_201_CREATED )
def create_posts(post: PostCreate, db: Session = Depends(get_db)):
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data": new_post}

# Delete a post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found")
    post.delete(synchronize_session=False)
    db.commit()
    
# Update a post
@app.put("/posts/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_post(id: int, post: PostUpdtae, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    old_post = post_query.first()
    if old_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found")
    post_query.update(post.model_dump(), synchronize_session=False)
    db.commit()
    return post_query.first()

# The end