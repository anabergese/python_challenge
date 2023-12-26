import pytest
from backend.src.domain.model import User

def make_User(id=1, name="Ricardo", username="Test User", email="test@io.io", phone="0000000000", website="www.test.com"):
    user_data = {
        "id": id,
        "name": name,
        "username": username,
        "email": email,
        "phone": phone,
        "website": website
    }
    return User(**user_data)

def test_can_create_User_model_with_valid_data():
    user = make_User(1, "Ana", "Bergese", "test@io.io", "123456", "www.test.com")
    assert isinstance(user, User)
    assert user.id == 1
    assert user.name == "Ana"
    assert user.username == "Bergese"
    assert user.email == "test@io.io"
    assert user.phone == "123456"
    assert user.website == "www.test.com"