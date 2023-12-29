from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from backend.src.repositories.jsonplaceholder_repository import (
    ApiPostRepository,
    ApiCommentRepository,
    ApiUserRepository,
)
from backend.src.domain.model import Post, User
from typing import Optional

app = FastAPI()


def handle_exception(e: Exception):
    raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts", response_model=list[Post])
async def read_all_posts(post_repository: ApiPostRepository = Depends()):
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
    post_repository: ApiPostRepository = Depends(),
    comment_repository: ApiCommentRepository = Depends(),
):
    try:
        post: Optional[Post] = await post_repository.get_by_id(post_id)
        comments = await comment_repository.get_comments_by_post_id(post_id)
        if post:
            post.comments = comments if comments else []
            return post
        else:
            raise HTTPException(status_code=404, detail="Post not found")
    except Exception as e:
        handle_exception(e)

@app.get("/users/{user_id}", response_model=User)
async def read_user_by_id(user_id: int, user_repository: ApiUserRepository = Depends()):
    try:
        user = await user_repository.get_by_id(user_id)
        if user:
            return user
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        handle_exception(e)