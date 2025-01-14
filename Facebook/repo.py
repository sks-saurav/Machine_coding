from collections import defaultdict, deque


class Repository:
    def __init__(self):
        self.users = {}
        self.connections = {}
        self.posts = {}
        self.feeds = defaultdict(deque)
