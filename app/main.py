
from fastapi import FastAPI, Response, status, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db
from sqlalchemy.dialects import postgresql

models.Base.metadata.create_all(bind=engine)

app = FastAPI()





class Post(BaseModel):# This the schema
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', dbname='FASTAPI', user='postgres', password='iw43pPa1t!ad', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection successfull!")
#         break
#     except Exception as error:
#         print("Connection to Database failed ", "Error: ", error)
#         time.sleep(5)





@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return{"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED )
def create_posts(post: Post):
    models.Post(title=post.title, content=post.content, published=post.published)
    return {"data": post}
    

# @app.get("/posts/{id}")
# def get_post(id: int):
#     cursor.execute("""Select * from posts where id = %s""", (str(id),))
#     post = cursor.fetchone()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found")
    
#     return {"data": post}

# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int):
#     cursor.execute("""delete from posts where id = %s returning *""", (str(id)))
#     post = cursor.fetchone()

#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found")
    
#     conn.commit()

# @app.put("/posts/{id}", status_code=status.HTTP_202_ACCEPTED)
# def update_post(id: int, post: Post):

#     cursor.execute("""UPDATE posts set title = %s, content = %s, published = %s where id = %s returning *""",
#                    (post.title, post.content, post.published, str(id)))
#     updated_post = cursor.fetchone()

#     if not updated_post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                            detail=f"Post with id: {id} not found")
#     conn.commit()
#     return updated_post

# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return{"data": posts}