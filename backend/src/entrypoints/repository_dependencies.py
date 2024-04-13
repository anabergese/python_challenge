from backend.src.repositories.jsonplaceholder_repository import (
    ApiPostRepository,
    ApiCommentRepository,
    ApiUserRepository,
)
from backend.src.repositories.repository import (
    CommentRepository,
    PostRepository,
    UserRepository,
)

def get_post_repository() -> PostRepository:
    return ApiPostRepository()

def get_comment_repository() -> CommentRepository:
    return ApiCommentRepository()

def get_user_repository() -> UserRepository:
    return ApiUserRepository()