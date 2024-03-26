import pytest
import httpx
from backend.src.services.jsonplaceholder_service import get_user_by_id, get_post_by_id, get_comments_by_post_id, fetch_data
from backend.tests.data_mocks import MockedUser
import unittest.mock as mock

class TestJsonPlaceholderService:

    @pytest.mark.asyncio
    async def test_get_user_by_id_success(self):
        data = await get_user_by_id(1)
        self.assert_user_data(data)

    @pytest.mark.asyncio
    async def test_get_user_with_invalid_id(self):
        with pytest.raises(httpx.HTTPStatusError) as exc_info:
            await get_user_by_id("string")

        self.assert_http_status_error(exc_info, 404)

    @pytest.mark.asyncio
    async def test_get_post_by_id_success(self):
        data = await get_post_by_id(1)
        self.assert_post_data(data)

    @pytest.mark.asyncio
    async def test_get_post_with_invalid_id(self):
        with pytest.raises(httpx.HTTPStatusError) as exc_info:
            await get_post_by_id("string")

        self.assert_http_status_error(exc_info, 404)

    @pytest.mark.asyncio
    async def test_get_comments_by_id_success(self):
        data = await get_comments_by_post_id(1)
        self.assert_comment_data(data)


    @pytest.mark.asyncio
    @mock.patch("backend.src.services.jsonplaceholder_service.httpx.AsyncClient.get")
    async def test_get_mocked_user_by_id(self, mock_get):
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = MockedUser
        mock_get.return_value = mock_response
        data = await get_user_by_id(1)
        assert data == MockedUser

    def assert_user_data(self, data):
        assert "id" in data
        assert "name" in data
        assert "username" in data
        assert "email" in data
        assert "phone" in data
        assert "website" in data

    def assert_post_data(self, data):
        assert "id" in data
        assert "userId" in data
        assert "title" in data
        assert "body" in data

    def assert_comment_data(self, data):
        assert "id" in data[0]
        assert "postId" in data[0]
        assert "name" in data[0]
        assert "email" in data[0]
        assert "body" in data[0]

    def assert_http_status_error(self, exc_info, expected_status_code):
        assert exc_info.value.response.status_code == expected_status_code
        assert isinstance(exc_info.value, httpx.HTTPStatusError)