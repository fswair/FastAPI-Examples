from time import time
from typing import Optional
from pydantic import BaseModel
from MentoDB import *

class MentoPostModel(BaseModel):
    post_id: PrimaryKey(int).set_primary()
    post_created_date: str
    post_created_unix: int
    post_author: str
    post_title: str
    post_description: str