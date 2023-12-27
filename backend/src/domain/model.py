from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    id: int
    name: str
    username: str
    email: EmailStr
    phone: str
    website: str

class Comment(BaseModel):
    id: int
    postId: int
    name: str
    email: EmailStr
    body: str

class Post(BaseModel):
    id: int
    userId: int = Field(..., gt=0)
    title: str
    body: str
    comments: list[Comment] | None = None
