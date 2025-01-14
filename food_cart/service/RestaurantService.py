from model.restaurant import  Restaurant
from model.user import Customer, Owner
from enums.sort import Sort
from model.Order import Order

class RestaurantService:
    def __init__(self, restaurant_repo, user_repo):
        self.restaurant_repo = restaurant_repo
        self.user_repo = user_repo

    def register_restaurant(self, user_name, restaurant_name, serviceable_pin, food_name, food_price, initial_quantity):
        user = self.user_repo.get_user(user_name)
        if not isinstance(user, Owner):
            raise Exception("The user don't own a restaurant")

        restaurant = Restaurant(restaurant_name, serviceable_pin, food_name, food_price, initial_quantity)
        self.restaurant_repo.add_restaurant(restaurant)
        self.user_repo.add_restaurant_to_user(user_name, restaurant_name)

    def update_quantity(self, restaurant_name, quantity_to_add):
        restaurant = self.restaurant_repo.get_restaurant(restaurant_name)
        restaurant.available_quantity += quantity_to_add

    def rate_restaurant(self, restaurant_name, rating_val):
        restaurant = self.restaurant_repo.get_restaurant(restaurant_name)
        restaurant.rating.add_rating(rating_val)

    def show_restaurant(self, sort_by=Sort.RATING):
        restaurant_list = self.restaurant_repo.get_all_restaurants()
        if sort_by == Sort.RATING:
            restaurant_list.sort(key=lambda x: x.food_price)
        elif sort_by == Sort.PRICE:
            restaurant_list.sort(key=lambda x: x.rating.get_average_rating())

        for res in restaurant_list:
            print(res)
        return restaurant_list

    def place_order(self, user_name, restaurant_name, quantity):
        user = self.user_repo.get_user(user_name)
        restaurant = self.restaurant_repo.get_restaurant(restaurant_name)

        if user.pin not in restaurant.serviceable_pin:
            raise Exception(f"Rertaurant {restaurant_name} not servicable in {user.pin} Area")

        if quantity > restaurant.available_quantity:
            raise  Exception("Desired quantity is not available")

        order = Order(user_name, restaurant_name, quantity)
        print("Order placed successfully!!")
        return  order




