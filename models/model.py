from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    username: str
    email: str
    phone: str
    website: str

class Post(BaseModel):
    id: int
    userId: int
    title: str
    body: str

class Comment(BaseModel):
    id: int
    postId: int
    name: str
    email: str
    body: str