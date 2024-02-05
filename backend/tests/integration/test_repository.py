from backend.src.repositories.repository import PostRepository, UserRepository
from backend.tests.data_mocks import MockedPosts, MockedPost, MockedUser
from backend.src.domain.model import Post, User
from typing import List, Optional

class TestFakeRepositories:

    @staticmethod
    def test_fake_post_repository_can_get_all_posts():
        fake_repo = FakePostRepository().get_all()
        assert fake_repo == MockedPosts

    @staticmethod
    def test_fake_post_repository_can_get_post():
        fake_repo = FakePostRepository().get_by_id(1)
        assert fake_repo == MockedPost

    @staticmethod
    def test_fake_user_repository_can_get_user():
        fake_repo = FakeUserRepository()
        result = fake_repo.get_by_id(1)
        assert result == MockedUser


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