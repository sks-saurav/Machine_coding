from collections import defaultdict
from enum import Enum

class User:
    def __init__(self, user_id, name, age, email):
        self.user_id  = user_id
        self.name = name
        self.age = age
        self.email = email

class Connection:
    def __init__(self, user_id):
        self.user_id = user_id
        self.friends = set()

class Reaction(Enum):
    LIKE = 1,
    DISLIKE = 2,
    LOVE = 3


class Post:
    def __init__(self, post_id, user_id, text, media):
        self.post_id = post_id
        self.user_id = user_id
        self.text = text
        self.media = media
        self.reactions = defaultdict(int)
        self.comments = []

    def __repr__(self):
        return f"({self.post_id}, {self.user_id}, {self.text}, {self.media})"

class Comment:
    def __init__(self, user_id, content):
        self.user_id = user_id
        self.content = content
        self.reactions = {}

class Feed:
    def __init__(self, user_id):
        self.user_id = user_id
        self.posts = []