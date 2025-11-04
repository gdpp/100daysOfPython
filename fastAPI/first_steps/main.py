from fastapi import Body, FastAPI, Query, HTTPException
from pydantic import BaseModel

app = FastAPI(title="mini-blog")

BLOG_POST = [
    {"id": 1, "title": "Hello from FastAPI", "content": "My first post with fast api"},
    {"id": 2, "title": "POST HTTP FastAPI", "content": "My second post with fast api"},
    {"id": 3, "title": "Django vs FastAPI", "content": "My third post with fast api"}
]

class Post(BaseModel):
    title: str
    content: str
    
@app.get("/")
def health():
    return {'message': 'Welcome to mini blog'}

@app.get("/posts")
def get_posts(query: str | None = Query(default=None, description="Search by title")):
    
    if query:
        
        results = [post for post in BLOG_POST if query.lower() in post["title"].lower()]
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
def create_post(post: Post):
    return {"data": post}
    # if not str(post["title"]).strip():
    #     return {"error": "Title cannot be empty"}
    
    # new_id = (BLOG_POST[-1]["id"] + 1) if BLOG_POST else 1
    
    # new_post = {"id": new_id, "title": post["title"], "content": post["content"]}
    # BLOG_POST.append(new_post)
    
    # return {"message": "Post Created", "data": new_post}

@app.put("/posts/{id}")
def update_post(id: int, data: dict = Body(...)):
    for post in BLOG_POST:
        if post["id"] == id:
            if "title" in data: post["title"] = data["title"]
            if "content" in data: post["content"] = data["content"]
            return {"message": "Updated post", "data": post}
        
    raise HTTPException(status_code=404, detail="Post not found")

@app.delete("/posts/{id}", status_code=204)
def delete_post(id: int):
    for idx, post in enumerate(BLOG_POST):
        if post["id"] == id:
            BLOG_POST.pop(idx)
            return
    
    raise HTTPException(status_code=404, detail="Post not found")