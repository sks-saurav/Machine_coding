from enums.Gender import Gender
from service.contextService import AppContext
from service.RestaurantService import RestaurantService
from service.UserService import UserService
from repository.RestaurantRepo import RestaurantRepo
from repository.UserRepo import UserRepo

def main():
    curr_context = AppContext()
    restaurant_repo = RestaurantRepo()
    user_repo = UserRepo()
    restaurant_service = RestaurantService(restaurant_repo=restaurant_repo, user_repo=user_repo)
    user_service = UserService(user_repo=user_repo)

    user_service.register_user("Saurav", Gender.MALE, '6205117662', 600081)
    user_service.register_user("Aish", Gender.FEMALE, '113517662', 500082, is_owner=True)

    curr_context.user_login("Aish")

    restaurant_service.register_restaurant(
        user_name=curr_context.user_name,
        restaurant_name="Kritunga",
        serviceable_pin=[500081, 500082],
        food_name="dosa",
        food_price=52,
        initial_quantity=50
    )

    restaurant_service.update_quantity(
        restaurant_name="Kritunga",
        quantity_to_add=12
    )

    restaurant_service.rate_restaurant(
        restaurant_name="Kritunga",
        rating_val=5
    )

    restaurant_service.show_restaurant()

    curr_context.user_login("Saurav")
    try:
        restaurant_service.place_order(
            user_name=curr_context.user_name,
            restaurant_name="Kritunga",
            quantity=130
        )
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()


