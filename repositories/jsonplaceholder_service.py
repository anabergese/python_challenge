import httpx

JSONPLACEHOLDER_API_URL = 'https://jsonplaceholder.typicode.com'

async def get_all_posts():
    url = f'{JSONPLACEHOLDER_API_URL}/posts'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.json()

async def get_post_by_id(id):
    url = f'{JSONPLACEHOLDER_API_URL}/posts/{id}'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.json()

async def get_all_comments():
    url = f'{JSONPLACEHOLDER_API_URL}/comments'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.json()

async def get_comment_by_id(id):
    url = f'{JSONPLACEHOLDER_API_URL}/comments/{id}'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.json()

async def get_comments_by_post_id(post_id):
    url = f'{JSONPLACEHOLDER_API_URL}/comments?postId={post_id}'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.json()

async def get_all_users():
    url = f'{JSONPLACEHOLDER_API_URL}/users'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.json()

async def get_user_by_id(id):
    url = f'{JSONPLACEHOLDER_API_URL}/users/{id}'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.json()