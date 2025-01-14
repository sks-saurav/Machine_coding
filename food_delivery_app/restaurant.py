class MenuItem:
    def __init__(self, item_id, name, price, category):
        self.id = item_id
        self.name = name
        self.price = price
        self.category = category

class Restaurant:
    def __init__(self, restaurant_id, name, address, cuisine, location, menu):
        self.id = restaurant_id
        self.name = name
        self.address = address
        self.cuisine = cuisine
        self.location = location  # (lat, long)
        self.menu = menu

class RestaurantManager:
    def __init__(self):
        self.restaurants = {}

    def register_restaurant(self, restaurant_id, name, address, cuisine, location, menu):
        if restaurant_id in self.restaurants:
            raise ValueError("Restaurant already exists")
        restaurant = Restaurant(restaurant_id, name, address, cuisine, location, menu)
        self.restaurants[restaurant_id] = restaurant
        return restaurant

    def get_menu(self, restaurant_id):
        restaurant = self.restaurants.get(restaurant_id)
        if not restaurant:
            raise ValueError("Restaurant not found")
        return restaurant.menu

    def suggest_restaurants(self, cuisine, max_delivery_time, user_location):
        suggested_restaurants = []
        for restaurant in self.restaurants.values():
            if restaurant.cuisine == cuisine:
                delivery_time_estimate = self._estimate_delivery_time(restaurant.location, user_location)
                if delivery_time_estimate <= max_delivery_time:
                    suggested_restaurants.append(restaurant)
        return suggested_restaurants

    def _estimate_delivery_time(self, restaurant_location, user_location):
        # Use distance to estimate delivery time
        distance = ((restaurant_location[0] - user_location[0]) ** 2 + (restaurant_location[1] - user_location[1]) ** 2) ** 0.5
        return distance * 10  # Example: 10 minutes per unit distance
