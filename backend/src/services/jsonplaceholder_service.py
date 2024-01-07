import httpx
from backend.src.domain.model import Post, Comment

JSONPLACEHOLDER_API_URL = "https://jsonplaceholder.typicode.com"


async def fetch_data(url):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
    except httpx.RequestError as req_err:
        print(f"Request error while fetching data from {url}: {req_err}")
        raise
    except httpx.HTTPStatusError as http_err:
        print(
            f"HTTP error ({http_err.response.status_code}) occurred while fetching data from {url}"
        )
        raise

def dict_to_post_model(post_dict: dict) -> Post:
    return Post(
        id=post_dict['id'],
        userId=post_dict['userId'],
        title=post_dict['title'],
        body=post_dict['body']
    )

def dict_to_comment_model(comment_dict: dict) -> Comment:
    return Comment(
        id=comment_dict['id'],
        postId=comment_dict['postId'],
        name=comment_dict['name'],
        email=comment_dict['email'],
        body=comment_dict['body']
    )
    
async def get_all_posts():
    url = f"{JSONPLACEHOLDER_API_URL}/posts"
    return await fetch_data(url)


async def get_post_by_id(id):
    url = f"{JSONPLACEHOLDER_API_URL}/posts/{id}"
    post_data = await fetch_data(url)
    if post_data:
        return dict_to_post_model(post_data)
    else:
        return None


async def get_all_comments():
    url = f"{JSONPLACEHOLDER_API_URL}/comments"
    return await fetch_data(url)


async def get_comment_by_id(id):
    url = f"{JSONPLACEHOLDER_API_URL}/comments/{id}"
    return await fetch_data(url)


async def get_comments_by_post_id(post_id):
    url = f"{JSONPLACEHOLDER_API_URL}/comments?postId={post_id}"
    comments_data = await fetch_data(url)
    return [dict_to_comment_model(comment_data) for comment_data in comments_data]



async def get_all_users():
    url = f"{JSONPLACEHOLDER_API_URL}/users"
    return await fetch_data(url)


async def get_user_by_id(id):
    url = f"{JSONPLACEHOLDER_API_URL}/users/{id}"
    return await fetch_data(url)
