from repositories.repository import PostRepository
from repositories.jsonplaceholder_service import get_all, get_by_id

class ApiPostRepository(PostRepository):
    def get_all(self):
        return get_all()
    
    def get_by_id(self, id):
        return get_by_id(id)