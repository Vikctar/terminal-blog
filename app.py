from database import Database
from models.post import Post

Database.initialize()

post = Post()

print(post.author)
