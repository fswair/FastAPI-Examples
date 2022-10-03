from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import HTMLResponse
import fastapi, uvicorn
from models import MentoPostModel
from schemas import Blog, ShowBlog, PostModel, UpdatePostModel
from functions import html_template
from database import db

has_data = lambda data: len(data) > 0

app = FastAPI()


@app.get("/post/{_post_id}", status_code=fastapi.status.HTTP_201_CREATED)
def home_page(_post_id: int, response: Response):
    response.status_code = fastapi.status.HTTP_200_OK
    return db.select("posts", filter=lambda post_id: post_id == _post_id)


@app.post("/post", status_code=fastapi.status.HTTP_201_CREATED)
def home_page(post: PostModel, response: Response):
    response.status_code = fastapi.status.HTTP_200_OK
    db.insert(
        "posts",
        data={
            "post_id": post.post_id,
            "post_created_date": post.post_created_date,
            "post_created_unix": post.post_created_unix,
            "post_author": post.post_author,
            "post_title": post.post_title,
            "post_description": post.post_description,
        },
    )

    return db.select("posts", where=dict(post_id=post.post_id))


@app.put("/post", status_code=fastapi.status.HTTP_200_OK)
def home_page(post: UpdatePostModel, response: Response):
    response.status_code = fastapi.status.HTTP_200_OK
    db.update(
        "posts",
        data={
            "post_id": post.new_post_id,
            "post_created_date": post.post_created_date,
            "post_created_unix": post.post_created_unix,
            "post_author": post.post_author,
            "post_title": post.post_title,
            "post_description": post.post_description,
        },
        where=dict(post_id=post.post_id),
    )

    return {
        "detail": "Content updated with new values.",
        "data": db.select("posts", where=dict(post_id=post.new_post_id)),
    }


@app.delete("/post/{post_id}", status_code=fastapi.status.HTTP_200_OK)
def home_page(post_id: int, response: Response):
    response.status_code = fastapi.status.HTTP_200_OK
    data = db.select("posts", where=dict(post_id=post_id))
    if has_data(data):
        db.delete("posts", where=dict(post_id=post_id))
        return {"detail": "Content deleted.", "data": "No data."}
    else:
        raise HTTPException(
            status_code=404, detail="Dont found content you want to see.."
        )


@app.get(
    "/posts", response_class=HTMLResponse, status_code=fastapi.status.HTTP_302_FOUND
)
def get_posts(response: Response):
    posts = db.select("posts")
    return HTMLResponse(html_template(posts))


uvicorn.run(app="main:app", reload=True)
