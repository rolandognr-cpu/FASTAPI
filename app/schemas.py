from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional, Annotated



class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class PostUpdtae(PostBase):
    title: str
    content: str
    published: bool


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut


class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(ge=0, le=1)]