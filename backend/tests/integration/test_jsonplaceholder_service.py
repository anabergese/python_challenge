import pytest
import httpx
from backend.src.services.jsonplaceholder_service import get_user_by_id

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


