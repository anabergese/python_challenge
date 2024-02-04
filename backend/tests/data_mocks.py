from backend.src.domain.model import Post, Comment, User

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