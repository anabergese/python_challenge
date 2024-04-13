from backend.src.repositories.jsonplaceholder_repository import (
    ApiPostRepository,
    ApiCommentRepository,
    ApiUserRepository,
)

def get_post_repository():
    return ApiPostRepository()

def get_comment_repository():
    return ApiCommentRepository()

def get_user_repository():
    return ApiUserRepository()