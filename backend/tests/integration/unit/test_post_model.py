import pytest
from backend.src.domain.model import Post
from pydantic import ValidationError


def make_post(id_value, userId=1, title="Test Post", body="This is a test post."):
    post_data = {
        "id": id_value,
        "userId": userId,
        "title": title,
        "body": body
    }
    return Post(**post_data)

def test_can_create_post_model_with_valid_data():
    post = make_post(1, 2, "Test Post", "This is a test post.")
    assert isinstance(post, Post)
    assert post.id == 1
    assert post.userId == 2
    assert post.title == "Test Post"
    assert post.body == "This is a test post."

def test_cannot_create_post_with_invalid_id_type():
    with pytest.raises(ValidationError):
        make_post("invalid_id", 2, "Test Post", "This is a test post.")

def test_cannot_create_post_with_invalid_userId_type():
    with pytest.raises(ValidationError):
        make_post(1, "invalid_userId", "Test Post", "This is a test post.")

def test_cannot_create_post_with_invalid_title_type():
    with pytest.raises(ValidationError):
        make_post(1, 2, 123, "This is a test post.")

def test_cannot_create_post_with_invalid_body_type():
    with pytest.raises(ValidationError):
        make_post(1, 2, "Test Post", 123)

# Review how to manage None values in Post model.
def test_cannot_create_post_without_required_id_field():
    with pytest.raises(ValidationError):
        make_post(None, 2, "Test Post", "This is a test post.")

def test_cannot_create_post_with_negative_userId():
    with pytest.raises(ValueError):
        make_post(1, -1, "Test Post", "This is a test post.")