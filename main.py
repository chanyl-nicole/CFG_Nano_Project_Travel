#
##
### THIS MODULE REPRESENTS THE CLIENT SIDE FOR OUR TRAVEL APP
##
#

# This is the code acting in the 'frontend'
# Main function that runs our travel app is = plan_your_trip() function

import requests # import requests library  = we can make requests to the API
import json

from db_utils import add_user_personal_items, remove_personal_items

from pprint import pprint as pp

def get_month_choices():
    result = requests.get(
        'http://127.0.0.1:5001/travel/months/',
        headers={'content-type': 'application/json'}
    )
    return result.json()

# test = get_month_choices()
# pp(test)
#[['August'], ['July'], ['June'], ['September']]


def get_cities():
    result = requests.get(
        'http://127.0.0.1:5001/travel/cities/',
        headers={'content-type': 'application/json'}
    )
    return result.json()

# test = get_cities()
# pp(test)


def get_city_weather(month):
    result = requests.get(
        'http://127.0.0.1:5001/travel/cities-weather-month/{}'.format(month),
        headers={'content-type': 'application/json'}
    )
    return result.json()

# test = get_city_weather('June')
# pp(test)


def get_essential_items(month, city):
    result = requests.get(
        'http://127.0.0.1:5001/travel/essential-items/{}/{}'.format(month, city),
        headers={'content-type': 'application/json'}
    )
    return result.json()

# test = get_essential_items('June', 'Paris')
# pp(test)


def get_personal_items():
    result = requests.get(
        'http://127.0.0.1:5001/travel/personal-items/',
        headers={'content-type': 'application/json'}
    )
    return result.json()


# test = get_personal_items()
# pp(test)

################    HELPER FUNCTION


def choose_month():
    """ This function allows the user to choose a month for
    their summer holidays and returns that month"""

    print ("Are you ready to book your summer holiday? You can travel in the following months: ")
    month_choices = get_month_choices()
    pp(month_choices)
    month = input("What month would you like to travel in? ")
# IMPORTANT for DEBUGGING AND TESTING:
    # here, if input is not a valid month, should raise an Exception!!!!
    # also, good case for testing what happens if we give the right or wrong input!
    return month

# choose_month()

################    HELPER FUNCTION

def choose_city(month):
    """ This function allows the user to choose a city for
    their summer holidays and returns that city"""

    print("The weather on the top 8 european destinations for {} is the following: ".format(month))
    city_weather = get_city_weather(month)
    for location in city_weather.keys():
        print(location, ':', '', city_weather[location])
    city = input("Which city would you like to go to: ")
 # IMPORTANT for DEBUGGING AND TESTING:
    # here, if input is not a valid city, should raise an Exception!!!!
    # also, good case for testing what happens if we give the right or wrong input!
    return city

# choose_city('June')

####################    HELPER FUNCTION

def add_personal_items():
    """ This function allows the user to add personal items
    needed for their holiday to the DB and returns a list of those items"""

    print("You can save a remainder list of up to 10 personal items to bring to your trip")
    user_items_list = []
    counter = 0
    while counter < 10:
        user_item = input("Please, enter item to be saved on list or enter 'done' when done: ")
        if user_item != 'done':
            user_items_list=[]
        # TESTING    ### Good case for testing! What happens if input is 'done' or another word
            if user_item not in user_items_list:
                user_items_list.append(user_item)
                add_user_personal_items(user_item)
                counter += 1
        else:
            #print(user_items_list)
            return user_items_list
    #print(user_items_list)
    return user_items_list

#add_personal_items()

#####################   MAIN FUNCTION

def plan_your_trip():
    """ This function allows the user to choose a month and city for their
    summer holidays and to create a remainder list of personal items to bring to their trip
    and returns these items plus suggested essential items for the chosen destination"""

    month = choose_month()
    city = choose_city(month)
    add_items = add_personal_items()
    personal_items = get_personal_items()
    clear_items = remove_personal_items()
    essential_items = get_essential_items(month, city)

    print("These are the suggested essential items for your trip: ")
    for i in essential_items:
        print(i)
    print("These are your saved personal items to bring to your trip: ")
    for i in personal_items:
        print(i)

    all_items = essential_items + personal_items

    return all_items

plan_your_trip() # Example input: Passport, Camera, Money, Asthma medication etc.

##### IDEAS OF EXTRA FUNCTIONALITY IF WE HAD TIME FOR REPORT:
    # In table of personal essential items in database, allow incorporating quantity of items needed
    # Allow deleting items from list/table of personal items in case usr input one by mistake or decides it is not longer needed