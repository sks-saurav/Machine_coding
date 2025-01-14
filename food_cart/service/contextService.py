class AppContext:
    def __init__(self):
        self.user_name = None

    def user_login(self, user_name):
        self.user_name = user_name