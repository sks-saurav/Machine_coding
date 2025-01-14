class Rating:
    def __init__(self):
        self.total_rating = 0
        self.user_rating_count = 0

    def get_average_rating(self):
        if self.user_rating_count == 0:
            return 0
        return self.total_rating / self.user_rating_count

    def add_rating(self, rating_val):
        self.total_rating += rating_val
        self.user_rating_count += 1