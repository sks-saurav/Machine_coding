class User:
    def __init__(self, name, gender, phone_number, pin):
        self.name = name
        self.gender = gender
        self.phone_number = phone_number
        self.pin = pin

class Owner(User):
    def __init__(self, name, gender, phone_number, pin):
        super().__init__(name, gender, phone_number, pin)
        self.restaurants = []

    def add_restaurant_name(self, restaurant_name):
        self.restaurants.append(restaurant_name)

class Customer(User):
    def __init__(self, name, gender, phone_number, pin):
        super().__init__(name, gender, phone_number, pin)

