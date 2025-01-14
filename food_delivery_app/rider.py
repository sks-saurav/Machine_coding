class Rider:
    def __init__(self, rider_id, name, vehicle_details, current_location):
        self.id = rider_id
        self.name = name
        self.vehicle_details = vehicle_details
        self.current_location = current_location  # (lat, long)

class RiderManager:
    def __init__(self):
        self.riders = {}

    def register_rider(self, rider_id, name, vehicle_details, current_location):
        if rider_id in self.riders:
            raise ValueError("Rider already exists")
        rider = Rider(rider_id, name, vehicle_details, current_location)
        self.riders[rider_id] = rider
        return rider

    def update_rider_location(self, rider_id, new_location):
        rider = self.riders.get(rider_id)
        if not rider:
            raise ValueError("Rider not found")
        rider.current_location = new_location

    def get_nearest_rider(self, restaurant_location):
        nearest_rider = None
        min_distance = float('inf')
        for rider in self.riders.values():
            distance = self._calculate_distance(restaurant_location, rider.current_location)
            if distance < min_distance:
                min_distance = distance
                nearest_rider = rider
        return nearest_rider

    def _calculate_distance(self, location1, location2):
        # Implement a distance calculation algorithm (e.g., Haversine formula)
        lat1, lon1 = location1
        lat2, lon2 = location2
        return ((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2) ** 0.5
