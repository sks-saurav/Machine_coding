class RestaurantRepo:
    def __init__(self):
        self.restaurants = {}

    def add_restaurant(self, restaurant):
        if restaurant.name in self.restaurants:
            print("Restaurant already added")
            return
        self.restaurants[restaurant.name] = restaurant

    def get_restaurant(self, restaurant_name):
        return self.restaurants[restaurant_name]

    def get_all_restaurants(self):
        return list(self.restaurants.values())