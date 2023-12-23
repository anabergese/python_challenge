from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from repositories.jsonplaceholder_repository import *
from models.model import Post, User

app = FastAPI()

def get_post_repository() -> PostRepository:
    return ApiPostRepository()

def get_comment_repository() -> CommentRepository:
    return ApiCommentRepository()

def get_user_repository() -> UserRepository:
    return ApiUserRepository()

def handle_exception(e: Exception):
    raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@app.get("/post-with-comments/{post_id}", response_model=dict)
async def get_post_with_comments(
    post_id: int,
    post_repository: PostRepository = Depends(get_post_repository),
    comment_repository: CommentRepository = Depends(get_comment_repository),
):
    try:
        post = await post_repository.get_by_id(post_id)
        if post:
            comments = await comment_repository.get_comments_by_post_id(post_id)
            post_with_comments = {
                "user_id": post["userId"],
                "id": post["id"],
                "title": post["title"],
                "body": post["body"],
                "comments": comments
            }
            return JSONResponse(content=post_with_comments)
        else:
            raise HTTPException(status_code=404, detail="Post not found")
    except Exception as e:
        handle_exception(e)

@app.get("/posts", response_model=list[Post])
async def read_all_posts(post_repository: PostRepository = Depends(get_post_repository)):
    try:
        posts = await post_repository.get_all()
        if posts:
            return JSONResponse(content=posts)
        else:
            raise HTTPException(status_code=404, detail="Posts not found")
    except Exception as e:
        handle_exception(e)
    
@app.get("/users/{user_id}", response_model=User)
async def read_user_by_id(user_id: int, user_repository: UserRepository = Depends(get_user_repository)):
    try:
        user = await user_repository.get_by_id(user_id)
        if user:
            return JSONResponse(content=user)
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        handle_exception(e)
