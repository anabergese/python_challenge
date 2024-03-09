import httpx
import logging

JSONPLACEHOLDER_API_URL = "https://jsonplaceholder.typicode.com"


async def fetch_data(url, timeout=40): 
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=timeout)
            response.raise_for_status()
            return response.json()
    except httpx.RequestError as req_err:
        logging.error(f"Request error while fetching data from {url}: {req_err}")
        raise
    except httpx.HTTPStatusError as http_err:
        logging.error(
            f"HTTP error ({http_err.response.status_code}) occurred while fetching data from {url}"
        )
        raise


async def get_resource_by_id(resource, resource_id=None):
    url = f"{JSONPLACEHOLDER_API_URL}/{resource}"
    if resource_id is not None:
        url += f"/{resource_id}"
    return await fetch_data(url)


async def get_all_posts():
    return await get_resource_by_id("posts")


async def get_post_by_id(post_id):
    return await get_resource_by_id("posts", post_id)


async def get_all_comments():
    return await get_resource_by_id("comments")


async def get_comments_by_post_id(post_id):
    return await get_resource_by_id("comments", f"?postId={post_id}")


async def get_comment_by_id(comment_id):
    return await get_resource_by_id("comments", comment_id)


async def get_post_with_comments(post_id):
    try:
        post = await get_resource_by_id("posts", post_id)
        comments = await get_resource_by_id("comments", f"?postId={post_id}")
        post['comments'] = comments
        return post
    except httpx.RequestError as req_err:
        logging.error(f"Request error while fetching post with comments (post_id={post_id}): {req_err}")
        raise
    except httpx.HTTPStatusError as http_err:
        logging.error(
            f"HTTP error ({http_err.response.status_code}) occurred while fetching post with comments (post_id={post_id})"
        )
        raise


async def get_user_by_id(user_id):
    return await get_resource_by_id("users", user_id)


async def get_all_users():
    return await get_resource_by_id("users")
