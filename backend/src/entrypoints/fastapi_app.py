from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.src.domain.model import Post, User
from backend.src.entrypoints.repository_dependencies import get_post_repository, get_user_repository
from backend.src.repositories.repository import (
    PostRepository,
    UserRepository,
)

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def handle_exception(e: Exception):
    raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@app.get("/posts", response_model=List[Post])
async def read_all_posts(post_repository: PostRepository = Depends(get_post_repository)):
    try:
        posts = await post_repository.get_all()
        if posts:
            return posts
        else:
            raise HTTPException(status_code=404, detail="Posts not found")
    except Exception as e:
        handle_exception(e)

@app.get("/post-with-comments/{post_id}", response_model=Post)
async def get_post_with_comments(
    post_id: int,
    post_repository: PostRepository = Depends(get_post_repository),
):
    try:
        post = await post_repository.get_post_with_comments(post_id)
        if post:
            return post
        else:
            raise HTTPException(status_code=404, detail="Post not found")
    except Exception as e:
        handle_exception(e)

@app.get("/users/{user_id}", response_model=User)
async def read_user_by_id(user_id: int, user_repository: UserRepository = Depends(get_user_repository)):
    try:
        user = await user_repository.get_by_id(user_id)
        if user:
            return user
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        handle_exception(e)