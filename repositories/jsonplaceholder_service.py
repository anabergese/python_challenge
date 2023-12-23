import httpx

JSONPLACEHOLDER_API_URL = 'https://jsonplaceholder.typicode.com'

async def get_all():
    url = f'{JSONPLACEHOLDER_API_URL}/posts'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.json()

async def get_by_id(id):
    url = f'{JSONPLACEHOLDER_API_URL}/posts/{id}'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.json()