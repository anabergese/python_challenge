from fastapi import Depends, FastAPI
from repositories.jsonplaceholder_repository import ApiPostRepository, PostRepository
from models.model import PostBase

app = FastAPI()

# Dependency to inject the data source (repository)
def get_post_repository() -> PostRepository:
    return ApiPostRepository()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/posts", response_model=list[PostBase])
async def read_all_posts(post_repository: PostRepository = Depends(get_post_repository)):
    posts = await post_repository.get_all()
    return posts