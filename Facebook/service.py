from entity import User, Comment, Connection, Post

class UserService:
    def __init__(self, repo):
        self.repo = repo

    def register_user(self, user_id, name, age, email):
        user = User(user_id, name, age, email)
        self.repo.users[user_id] = user
        self.repo.connections[user_id] = Connection(user_id)
        print(f'user {user_id} registered successfully')

    def follow(self, user_id1, user_id2):
        self.repo.connections[user_id1].friends.add(user_id2)
        print(f'{user_id2} started following {user_id1}')

    def unfollow(self, user_id1, user_id2):
        try:
            self.repo.connections[user_id1].friends.remove(user_id2)
            print(f'{user_id2} unfollowed {user_id1}')
        except Exception as e:
            print("invalid Operations!!")


class PostService:
    def __init__(self, repo):
        self.repo = repo

    def create_post(self, user_id, post_id, text, media):
        post = Post(post_id, user_id, text, media)
        self.repo.posts[post_id] = post
        print("Post created")

    def delete_post(self, post_id):
        try:
            del self.repo.posts[post_id]
            print('post deleted successfully')
        except Exception as e:
            print('user_id or post_id doesnt exists')

    def like_post(self, post_id, reaction):
        if post_id in self.repo.posts:
            post = self.repo.posts[post_id]
            post.reactions[reaction] += 1
            print("liked the post")
        else:
            print('post not found!!')

    def make_comment(self, post_id, user_id, content):
        comment = Comment(user_id, content)
        if post_id in self.repo.posts:
            post = self.repo.posts[post_id]
            post.comments.append(comment)
            print("Commented on the post")
        else:
            print('post not found!!')

class FeedService:
    def __init__(self, repo):
        self.repo = repo

    def generate_feed(self, user_id):
        friend_set = self.repo.connections[user_id].friends

        friends_post = []
        for post_id in self.repo.posts:
            post = self.repo.posts[post_id]
            if post.user_id in friend_set:
                friends_post.append(post)
        return friends_post

    def get_paginated_feed(self, user_id, page_size):
        if (self.repo.feeds[user_id]) == 0:
            self.generate_feed(user_id)

        result = []
        user_feed = self.repo.feeds[user_id]
        for _ in range(page_size):
            result.append(user_feed.popleft())

        return result



