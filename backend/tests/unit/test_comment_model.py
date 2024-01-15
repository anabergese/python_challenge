from backend.src.domain.model import Comment

def make_comment(id=1, name="Ricardo", postId=1 , email="test@io.io", body="Some text"):
    comment_data = {
        "id": id,
        "name": name,
        "postId": postId,
        "email": email,
        "body": body,
    }
    return Comment(**comment_data)

def test_can_create_Comment_model_with_valid_data():
    comment = make_comment(1, "Ana", 2, "test@io.io", "Random text")
    assert isinstance(comment, Comment)
    assert comment.id == 1
    assert comment.postId == 2
    assert comment.name == "Ana"
    assert comment.email == "test@io.io"
    assert comment.body == "Random text"
