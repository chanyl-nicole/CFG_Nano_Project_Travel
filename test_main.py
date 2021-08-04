from db_utils import show_cities, show_months


def choose_city():
    print("Are you ready to book a holiday? You can travel to:")
    city_choices = show_cities()
    print(city_choices)
    user_choice_city = input("Which city would you  like to go to: ")
    return user_choice_city


def choose_month():
    print("You can travel in the following months:")
    month_choices = show_months()
    print(month_choices)
    user_choice_month = input("What month would you like to travel in? ")
    return user_choice_month

