from model.user import Customer, Owner

class UserService:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def register_user(self, name, gender, phone, pincode, is_owner=False):
        user = None
        if is_owner:
            user = Owner(name, gender, phone, pincode)
        else:
            user = Customer(name, gender, phone, pincode)

        self.user_repo.add_user(user)
