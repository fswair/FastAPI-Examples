from pydantic import BaseModel
from typing import Optional
from time import time
class Blog(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    alias: Optional[str] = None
    author: str
    status: bool


class ShowBlog(BaseModel):
    title: str
    description: str
    author: str


class Post:
    def __init__(self, post_id: int = None, post_created_date: str = None, post_created_unix: Optional[int|float] = time(),  post_author: str = None, post_title: str = None, post_description: str = None):
        self.post_id: int = post_id 
        self.post_created_date: str = post_created_date
        self.post_created_unix: Optional[int|float] = post_created_unix
        self.post_author: str = post_author
        self.post_title: str = post_title
        self.post_description: str = post_description



class PostModel(BaseModel):
    post_id: int
    post_created_date: str
    post_created_unix: Optional[int|float] = time()
    post_author: str
    post_title: str
    post_description: str

class UpdatePostModel(BaseModel):
    post_id: int
    new_post_id: int
    post_created_date: str
    post_created_unix: Optional[int|float] = time()
    post_author: str
    post_title: str
    post_description: str