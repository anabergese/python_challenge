import pytest
from backend.src.repositories.jsonplaceholder_service import get_user_by_id

@pytest.mark.asyncio
async def test_get_user_by_id_success():
    data = await get_user_by_id(1)
    assert "id" in data
    assert "name" in data
    assert "username" in data
    assert "email" in data
    assert "phone" in data
    assert "website" in data