from fastapi import Depends, FastAPI, HTTPException
from repositories.jsonplaceholder_repository import *
from models.model import Post, User

app = FastAPI()

def get_post_repository() -> PostRepository:
    return ApiPostRepository()

def get_comment_repository() -> CommentRepository:
    return ApiCommentRepository()

def get_user_repository() -> UserRepository:
    return ApiUserRepository()

@app.get("/post-with-comments/{post_id}", response_model=dict)
async def get_post_with_comments(
    post_id: int,
    post_repository: PostRepository = Depends(get_post_repository),
    comment_repository: CommentRepository = Depends(get_comment_repository),
):
    post = await post_repository.get_by_id(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    comments = await comment_repository.get_comments_by_post_id(post_id)

    post_with_comments = {
        "user_id": post["userId"],
        "id": post["id"],
        "title": post["title"],
        "body": post["body"],
        "comments": comments
    }

    return post_with_comments

@app.get("/posts", response_model=list[Post])
async def read_all_posts(post_repository: PostRepository = Depends(get_post_repository)):
    posts = await post_repository.get_all()
    return posts

@app.get("/users/{user_id}", response_model=User)
async def read_user_by_id(user_id: int, user_repository: UserRepository = Depends(get_user_repository)):
    user = await user_repository.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user