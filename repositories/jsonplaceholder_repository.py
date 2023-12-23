from repositories.repository import PostRepository, CommentRepository, UserRepository
from repositories.jsonplaceholder_service import *
class ApiPostRepository(PostRepository):
    def get_all(self):
        return get_all_posts()
    
    def get_by_id(self, id):
        return get_post_by_id(id)

class ApiCommentRepository(CommentRepository):
    def get_all(self):
        return get_all_comments()
    
    def get_by_id(self, id):
        return get_comment_by_id(id)
    
    def get_comments_by_post_id(self, post_id):
        return get_comments_by_post_id(post_id)
    
class ApiUserRepository(UserRepository):
    def get_all(self):
        return get_all_users()
    
    def get_by_id(self, id):
        return get_user_by_id(id)