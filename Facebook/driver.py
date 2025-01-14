'''
PROBLEM STATEMENT:
Design Facebook APIs (Create Post, Delete Post, Get Feed, Get Feed Paginated, Follow, Unfollow).
Machine coding round with few test cases around it which you need to clear.
Use of 1-2 design patterns is recommended

Actor:
Entity:
User
Connection
Post
Feed
FacebookSevide
Repo
'''

from entity import User, Comment, Connection, Post
from repo import Repository
from service import PostService, UserService, FeedService

repo = Repository()
post_service = PostService(repo)
feed_service = FeedService(repo)
user_service = UserService(repo)


user_service.register_user(1, 'saurav', 12, 'saurav@gmail.com')
user_service.register_user(2, 'gaurav', 12, 'saurav@gmail.com')
user_service.register_user(3, 'ankit', 12, 'saurav@gmail.com')
user_service.register_user(4, 'aishwarya', 12, 'saurav@gmail.com')

user_service.follow(1, 2)
user_service.follow(2, 1)
user_service.follow(3, 1)
user_service.follow(2, 3)
user_service.follow(1, 4)
user_service.follow(2, 4)
user_service.unfollow(2, 4)

post_service.create_post(1, 1, 'Hello world', "image1.png")
post_service.create_post(1, 2, 'bye  world', "video.mp4")

posts = feed_service.generate_feed(2)
print(posts)