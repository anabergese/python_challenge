import pytest
from fastapi.testclient import TestClient
from backend.src.entrypoints.fastapi_app import app, handle_exception
from backend.src.domain.model import Post, Comment

client = TestClient(app)

MockedPosts = [
    Post(userId=1, id=1, title="Mocked Post 1", body="Mocked Body 1").model_dump(),
    Post(userId=1, id=2, title="Mocked Post 2", body="Mocked Body 2").model_dump(),
]

MockedComments = [
    Comment(body='Mocked Body 1', email='test@io.io', id=1, name='Mocked Name 1', postId=1),
    Comment(body='Mocked Body 1', email='test@io.io', id=2, name='Mocked Name 2', postId=1),
]

MockedPost = Post(userId=1, id=1, title="Mocked Post 1", body="Mocked Body 1", comments=MockedComments)

MockedUser = {
    'id': 1,
    'name': 'Mocked User 1',
    'username': 'mocked_username',
    'email': 'mocked@email.com',
    'phone': '123456789',
    'website': 'https://example.com'
}

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_read_all_posts(mocker):
    mocker.patch("backend.src.entrypoints.fastapi_app.ApiPostRepository.get_all", return_value=MockedPosts)

    response = client.get("/posts")
    assert response.status_code == 200
    assert response.json() == MockedPosts

def test_read_user_by_id(mocker):
    mocker.patch("backend.src.entrypoints.fastapi_app.ApiUserRepository.get_by_id", return_value=MockedUser)

    response = client.get("/users/1")
    assert response.status_code == 200
    user_from_response = response.json()
    assert user_from_response == MockedUser

def test_cannot_read_with_invalid_user_id_type(mocker):
    mocker.patch("backend.src.entrypoints.fastapi_app.ApiUserRepository.get_by_id", return_value=MockedUser)

    response = client.get("/users/invalid_id")
    assert response.status_code == 422
    response_data = response.json()
    detail = response_data["detail"][0]
    assert detail["type"] == "int_parsing"
    assert detail["msg"] == "Input should be a valid integer, unable to parse string as an integer"
    assert detail["input"] == "invalid_id"

def test_cannot_read_inexistent_user_id():    
    response = client.get("/users/1234567890")
    assert response.status_code == 500
    response_data = response.json()
    detail = response_data["detail"]
    assert detail == "Internal Server Error: Client error '404 Not Found' for url 'https://jsonplaceholder.typicode.com/users/1234567890'\nFor more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404"

def test_get_post_with_comments(mocker):
    try:
        mocker.patch("backend.src.entrypoints.fastapi_app.ApiPostRepository.get_by_id", return_value=MockedPost)
        mocker.patch("backend.src.entrypoints.fastapi_app.ApiCommentRepository.get_comments_by_post_id", return_value=MockedComments)
        if MockedPost:
            MockedPost.comments = MockedComments if MockedComments else []
        else:
            raise Exception("Post not found error")
    except Exception as e:
        handle_exception(e)

    if MockedPost:
        response = client.get("/post-with-comments/13")
        assert response.status_code == 200
        response_data = response.json()

        # Convert comments in the response to Comment instances
        response_comments_data = response_data.get('comments', [])
        response_comments = [Comment(**comment) for comment in response_comments_data]

        assert response_data['id'] == MockedPost.id
        assert response_data['userId'] == MockedPost.userId
        assert response_data['title'] == MockedPost.title
        assert response_data['body'] == MockedPost.body
        assert response_comments == MockedPost.comments

# https://fastapi.tiangolo.com/tutorial/testing/
# def test_cannot_get_post_with_comments_with_invalid_post_id_type()
# def test_cannot_get_post_with_comments_with_inexistent_post_id()
