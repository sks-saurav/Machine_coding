class User:
    def __init__(self, user_id, name, address, phone_number):
        self.id = user_id
        self.name = name
        self.address = address
        self.phone_number = phone_number

class UserManager:
    def __init__(self):
        self.users = {}

    def register_user(self, user_id, name, address, phone_number):
        if user_id in self.users:
            raise ValueError("User already exists")
        user = User(user_id, name, address, phone_number)
        self.users[user_id] = user
        return user

    def get_user(self, user_id):
        return self.users.get(user_id)
