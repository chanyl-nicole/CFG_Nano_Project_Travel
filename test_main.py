from db_utils import show_cities, show_months, show_essential_items


def choose_city():
    print("Are you ready to book a holiday? You can travel to:")
    city_choices = show_cities()
    print(city_choices)
    city = input("Which city would you  like to go to: ")
    return city


def choose_month():
    print("You can travel in the following months:")
    month_choices = show_months()
    print(month_choices)
    month = input("What month would you like to travel in? ")
    return month


def show_items():
    city = choose_city()
    month = choose_month()
    items = show_essential_items(month, city)
    print(f"You need to  bring: {items}")
    return items


show_items()




