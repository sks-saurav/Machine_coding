class Order:
    def __init__(self, order_id, user_id, restaurant_id, rider_id, menu_items, status, delivery_time_estimate):
        self.id = order_id
        self.user_id = user_id
        self.restaurant_id = restaurant_id
        self.rider_id = rider_id
        self.menu_items = menu_items
        self.status = status
        self.delivery_time_estimate = delivery_time_estimate

class OrderManager:
    def __init__(self):
        self.orders = {}

    def place_order(self, order_id, user_id, restaurant_id, menu_items, rider_id, delivery_time_estimate):
        order = Order(order_id, user_id, restaurant_id, rider_id, menu_items, "Pending", delivery_time_estimate)
        self.orders[order_id] = order
        return order

    def get_order_history_by_user(self, user_id):
        return [order for order in self.orders.values() if order.user_id == user_id]

    def get_order_history_by_rider(self, rider_id):
        return [order for order in self.orders.values() if order.rider_id == rider_id]
