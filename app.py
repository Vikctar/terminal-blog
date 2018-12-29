from database import Database
from models.blog import Blog
from models.post import Post

Database.initialize()

post = Post.from_mongo('b1c95b9aeb364627ad87168cde32b31f')
# print(post)

posts = Post.from_blog('123')

blog = Blog(author='Vikc',
            title='New New',
            description='New description')

blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

print(blog.get_posts())
