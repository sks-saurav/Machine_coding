from model.rating import Rating

class Restaurant:
    def __init__(self, name, serviceable_pin, food_name, food_price, intial_quantity):
        self.name = name
        self.serviceable_pin = serviceable_pin
        self.food_name = food_name
        self.food_price = food_price
        self.available_quantity = intial_quantity
        self.rating = Rating()

    def __repr__(self):
        return f'name: {self.name}, food_item: {self.food_name}, rating: {self.rating.get_average_rating()}'
