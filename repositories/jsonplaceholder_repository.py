from typing import List, Optional
from models.model import Post, Comment, User
from repositories.repository import PostRepository, CommentRepository, UserRepository
from repositories.jsonplaceholder_service import (
    get_all_posts,
    get_post_by_id,
    get_all_comments,
    get_comment_by_id,
    get_comments_by_post_id,
    get_all_users,
    get_user_by_id,
)


class ApiPostRepository(PostRepository):
    async def get_all(self) -> List[Post]:
        return await get_all_posts()

    async def get_by_id(self, post_id: int) -> Optional[Post]:
        return await get_post_by_id(post_id)


class ApiCommentRepository(CommentRepository):
    async def get_all(self) -> List[Comment]:
        return await get_all_comments()

    async def get_by_id(self, comment_id: int) -> Optional[Comment]:
        return await get_comment_by_id(comment_id)

    async def get_comments_by_post_id(self, post_id: int) -> List[Comment]:
        return await get_comments_by_post_id(post_id)


class ApiUserRepository(UserRepository):
    async def get_all(self) -> List[User]:
        return await get_all_users()

    async def get_by_id(self, user_id: int) -> Optional[User]:
        return await get_user_by_id(user_id)
