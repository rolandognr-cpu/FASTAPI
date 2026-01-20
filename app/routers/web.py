from fastapi import APIRouter, responses
from pathlib import Path

router = APIRouter(
    prefix="/web",
    tags=['Web']
)
base_dir = Path(__file__).resolve().parent.parent

# Retrieve all posts
@router.get("/", )
async def get_posts():
    file_path = base_dir / "templates" / "index.html"
    return responses.FileResponse(file_path)
    
    

# # Retrieve posts by id
# @router.get("/{id}", response_model=Post)
# def get_post(id: int, db: Session = Depends(get_db)):
#     post = db.query(models.Post).filter(models.Post.id == id).first()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found")
#     return post

# # Create a post
# @router.post("/", status_code=status.HTTP_201_CREATED, response_model=Post)
# def create_posts(post: PostCreate, db: Session = Depends(get_db)):
#     new_post = models.Post(**post.model_dump())
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)
#     return new_post

# # Delete a post
# @router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int, db: Session = Depends(get_db)):
#     post = db.query(models.Post).filter(models.Post.id == id)
#     if post.first() == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found")
#     post.delete(synchronize_session=False)
#     db.commit()
    
# # Update a post
# @router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=Post)
# def update_post(id: int, post: PostUpdtae, db: Session = Depends(get_db)):
#     post_query = db.query(models.Post).filter(models.Post.id == id)
#     old_post = post_query.first()
#     if old_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found")
#     post_query.update(post.model_dump(), synchronize_session=False)
#     db.commit()
#     return post_query.first()