from fastapi import status, HTTPException, Depends, APIRouter, Response, responses
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import models
from ..database import get_db
from ..schemas import UserLogin
from ..utils import verify
from ..oauth2 import create_access_token
from pathlib import Path


router = APIRouter(tags=['Authentication'])

base_dir = Path(__file__).resolve().parent.parent


@router.get('/login')
async def serve_login():
    file_path = base_dir / "templates" / "login.html"
    return responses.FileResponse(file_path)


@router.post('/login')
def login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid credentials')
    
    if not verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid credentials')
    
    # Create a token
    access_token = create_access_token(data={"user_id": user.id})

    # return token
    return Response(
        content= '{"access_token": {access_token}, "token_type": "bearer"}', 
        media_type="application/json",
        headers={"X-Redirect-URL": "/users"}
    )


    # return {"sccess_token": access_token,
    #         "token_type": "bearer"}