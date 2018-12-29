from database import Database
from models.post import Post

Database.initialize()

post = Post.from_mongo('b1c95b9aeb364627ad87168cde32b31f')
print(post)

posts = Post.from_blog('123')
for p in posts:
    print(p)
