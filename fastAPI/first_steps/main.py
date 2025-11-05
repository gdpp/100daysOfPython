from fastapi import Body, FastAPI, Query, HTTPException
from pydantic import BaseModel, Field, field_validator
from typing import Optional

app = FastAPI(title="mini-blog")

BLOG_POST = [
    {"id": 1, "title": "Hello from FastAPI",
        "content": "My first post with fast api"},
    {"id": 2, "title": "POST HTTP FastAPI",
        "content": "My second post with fast api"},
    {"id": 3, "title": "Django vs FastAPI",
        "content": "My third post with fast api"}
]


class PostBase(BaseModel):
    title: str
    content: Optional[str] = "Default content"


class PostCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Post title (3 character minimum and maximum 100)",
        examples=["My first post with FastAPI"]
    )
    content: Optional[str] = Field(
        default="Default content",
        min_length=10,
        description="Post content (10 characters minimum)",
        examples=["This is a valid post content cuz its greater than 10 chars"]
    )

    @field_validator("title")
    @classmethod
    def not_allowed_title(cls, value: str) -> str:
        for word in ["spam", "xxx", "terrorism", "porn"]:
            if word in value.lower():
                raise ValueError(f"Word {word} not allowed in title field")
        return value


class PostUpdate(BaseModel):
    title: str
    content: Optional[str] = None


@app.get("/")
def health():
    return {'message': 'Welcome to mini blog'}


@app.get("/posts")
def get_posts(query: str | None = Query(default=None, description="Search by title")):

    if query:

        results = [post for post in BLOG_POST if query.lower()
                   in post["title"].lower()]
        # for post in BLOG_POST:
        #     if query.lower() in post["title"].lower():
        #         results.append(post)

        return {"data": results, "query": query}

    return {"data": BLOG_POST}


@app.get('/posts/{id}')
def get_post_by_id(id: int, include_content: bool = Query(default=True, description="Include content flag")):
    for post in BLOG_POST:
        if post["id"] == id:
            if not include_content:
                return {"data": {"id": post["id"], "title": post["title"]}}

            return {"data": post}

    return {"error": "Post Not Found"}


@app.post("/posts")
def create_post(post: PostCreate):
    new_id = (BLOG_POST[-1]["id"] + 1) if BLOG_POST else 1
    new_post = {"id": new_id, "title": post.title, "content": post.content}
    BLOG_POST.append(new_post)

    return {"message": "Post Created", "data": new_post}


@app.put("/posts/{id}")
def update_post(id: int, data: PostUpdate = Body(...)):
    for post in BLOG_POST:
        if post["id"] == id:
            payload = data.model_dump(exclude_unset=True)
            if "title" in payload:
                post["title"] = payload["title"]
            if "content" in payload:
                post["content"] = payload["content"]
            return {"message": "Updated post", "data": post}

    raise HTTPException(status_code=404, detail="Post not found")


@app.delete("/posts/{id}", status_code=204)
def delete_post(id: int):
    for idx, post in enumerate(BLOG_POST):
        if post["id"] == id:
            BLOG_POST.pop(idx)
            return

    raise HTTPException(status_code=404, detail="Post not found")
