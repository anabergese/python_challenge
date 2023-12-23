from abc import ABC, abstractmethod

class BaseRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def get_by_id(self, id):
        pass
    
class PostRepository(BaseRepository):
    pass