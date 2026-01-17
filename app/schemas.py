from pydantic import BaseModel


class PostBase(BaseModel):# This the schema
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class PostUpdtae(PostBase):# This the schema
    title: str
    content: str
    published: bool