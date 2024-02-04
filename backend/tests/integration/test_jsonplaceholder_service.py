import pytest
import httpx
from backend.src.services.jsonplaceholder_service import get_user_by_id, get_post_by_id, get_comments_by_post_id
from backend.tests.data_mocks import MockedUser
import unittest.mock as mock

@pytest.mark.asyncio
async def test_get_user_by_id_success():
    data = await get_user_by_id(1)
    assert "id" in data
    assert "name" in data
    assert "username" in data
    assert "email" in data
    assert "phone" in data
    assert "website" in data
    
@pytest.mark.asyncio
async def test_get_user_with_invalid_id():
    with pytest.raises(httpx.HTTPStatusError) as exc_info:
        await get_user_by_id("string") 

    assert exc_info.value.response.status_code == 404
    assert isinstance(exc_info.value, httpx.HTTPStatusError)

@pytest.mark.asyncio
async def test_get_post_by_id_success():
    data = await get_post_by_id(1)
    assert "id" in data
    assert "userId" in data
    assert "title" in data
    assert "body" in data

@pytest.mark.asyncio
async def test_get_post_with_invalid_id():
    with pytest.raises(httpx.HTTPStatusError) as exc_info:
        await get_post_by_id("string") 

    assert exc_info.value.response.status_code == 404
    assert isinstance(exc_info.value, httpx.HTTPStatusError)

@pytest.mark.asyncio
async def test_get_comments_by_id_success():
    data = await get_comments_by_post_id(1)
    assert "id" in data[0]
    assert "postId" in data[0]
    assert "name" in data[0]
    assert "email" in data[0]
    assert "body" in data[0]

@pytest.mark.asyncio
async def test_get_comments_with_invalid_id():
    data = await get_comments_by_post_id("string") 
    assert data == []


@mock.patch("backend.src.services.jsonplaceholder_service.httpx.AsyncClient.get")
def get_mocked_user_by_id(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = MockedUser
    mock_get.return_value = mock_response
    data = get_user_by_id(1)
    assert data == MockedUser
