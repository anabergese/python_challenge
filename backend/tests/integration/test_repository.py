from backend.src.repositories.repository import PostRepository, UserRepository
from backend.src.domain.model import Post, Comment, User
from typing import List, Optional

MockedPosts = [
    Post(userId=1, id=1, title="Mocked Post 1", body="Mocked Body 1").model_dump(),
    Post(userId=1, id=2, title="Mocked Post 2", body="Mocked Body 2").model_dump(),
]

MockedComments = [
    Comment(body='Mocked Body 1', email='test@io.io', id=1, name='Mocked Name 1', postId=1).model_dump(),
    Comment(body='Mocked Body 1', email='test@io.io', id=2, name='Mocked Name 2', postId=1).model_dump(),
]

MockedPost = Post(userId=1, id=1, title="Mocked Post 1", body="Mocked Body 1", comments=MockedComments).model_dump()

MockedUser = {
    'id': 1,
    'name': 'Mocked User 1',
    'username': 'mocked_username',
    'email': 'mocked@email.com',
    'phone': '123456789',
    'website': 'https://example.com'
}
class FakePostRepository(PostRepository):
    def get_all(self) -> List[Post]:
        return MockedPosts

    def get_by_id(self, post_id) -> Optional[Post]:
        return MockedPost

class FakeUserRepository(UserRepository):
    def get_all(self) -> List[User]:
        return [MockedUser]
    
    def get_by_id(self, user_id) -> Optional[User]:
        return MockedUser
    
def test_fake_post_repository_can_get_all_posts():
    fakeRepo = FakePostRepository().get_all()
    assert fakeRepo == MockedPosts

def test_fake_post_repository_can_get_post():
    fakeRepo = FakePostRepository().get_by_id(1)
    assert fakeRepo == MockedPost

def test_fake_user_repository_can_get_user():
    fake_repo = FakeUserRepository()
    result = fake_repo.get_by_id(1)
    assert result == MockedUser