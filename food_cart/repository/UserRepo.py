class UserRepo:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        if user.name in self.users:
            print("User already present")
            return
        self.users[user.name] = user

    def get_user(self, user_name):
        if user_name not in self.users:
            raise Exception("user not found")
        return self.users[user_name]

    def add_restaurant_to_user(self, user_name, restaurant_name):
        user = self.get_user(user_name)
        user.add_restaurant_name(restaurant_name)

