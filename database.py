from MentoDB import *
from models import MentoPostModel

connection = MentoConnection("./database/database.db", check_same_thread=False)

db = Mento(connection)

db.create("posts", model=MentoPostModel)
