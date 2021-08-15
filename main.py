### THIS MODULE REPRESENTS THE CLIENT SIDE FOR OUR TRAVEL APP

# This is the code acting in the 'frontend'
# Main function that runs our travel app is = plan_your_trip() function

import requests
from db_utils import add_user_personal_items, remove_personal_items,get_country
from pprint import pprint as pp

def view_country():
    result = requests.get(
        'http:/127.0.0.1:5001/country',
        headers={'content-type': 'application/json'}
    )
    return result.json()
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

    print("Are you ready to book your summer holiday? You can travel in the following months: ")
    month_choices = get_month_choices()
    months = []
    for month in month_choices:
        print('-', month[0])
        months.append(month[0])
    # print(months)
    month = input("What month would you like to travel in? ").capitalize().strip()
    while month not in months:
        print(f'You cannot travel in {month.title()}')
        month = input("Please choose a valid month to travel in: ").capitalize().strip()
    else:
        return month
    # IMPORTANT for DEBUGGING AND TESTING:
    # here, if input is not a valid month, should raise an Exception!!!!
    # also, good case for testing what happens if we give the right or wrong input!

# choose_month()



################    HELPER FUNCTION


def choose_city(month):
    """ This function allows the user to choose a city for
       their summer holidays and returns that city"""

    print("\nThe weather in the top 8 European destinations for {} is the following: ".format(month))
    city_weather = get_city_weather(month)
    for location in city_weather.keys():
        print(location, ':', '', city_weather[location])
    city = input("\nWhich city would you like to go to: ").capitalize().strip()
    while city not in city_weather.keys():
        print(f'You cannot travel to {city.title()}')
        city = input("Please choose a valid city to travel to: ").capitalize().strip()
    else:
        return city

    # IMPORTANT for DEBUGGING AND TESTING:
    # here, if input is not a valid city, should raise an Exception!!!!
    # also, good case for testing what happens if we give the right or wrong input!
    """ This function allows the user to choose a city for
    their summer holidays and returns that city"""


# choose_city('June')

####################    HELPER FUNCTION


def get_covid_info(city):

    res = get_country(city)
    url = "https://api.traveladviceapi.com/search/{}".format(','.join(*res))
    payload = {}
    headers = {
        'X-Access-Token': '5f50fb53-5bca-4cc1-a2d7-7ee99a98fc8a'
    }
    # ee538d1a-ffac-462e-94f3-1b3710691e29 #orginal key

    response = requests.request("GET", url, headers=headers, data=payload)
    json_result = response.json()
    the_city = json_result.get(['trips'][0])
    country = ''.join(x for x in the_city[0]['to'])
    restrictions = json_result['trips'][0]['advice']['restrictions']
    print(f'\nCurrent COVID-19 restriction in {country}: ')
    for key, value in restrictions.items():

        for i, x in restrictions.get(key).items():
            print(key.upper(), ": \n{:<10} {:<10} ".format(i, x))
    return restrictions

####### HELPER FUNCTION
def add_personal_items():
    """ This function allows the user to add personal items
    needed for their holiday to the DB and returns a list of those items"""

    print("\nYou can save a reminder list of up to 10 personal items to bring on your trip.")
    user_items_list = []
    counter = 0
    while counter < 10:
        user_item = input("Please enter item to be saved on your personal list or enter 'done' when done: ").capitalize().strip()
        if user_item != 'Done':
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

def main():
    """ This function allows the user to choose a month and city for their
        summer holidays and to create a remainder list of personal items to bring to their trip
        and returns these items plus suggested essential items for the chosen destination"""

    month = choose_month()
    city = choose_city(month)
    # covid = get_covid_info(city)
    add_items = add_personal_items()
    personal_items = get_personal_items()
    clear_items = remove_personal_items()
    essential_items = get_essential_items(month, city)

    print("\nThese are the suggested essential items for your trip: ")
    for item in essential_items:
        print('-', item[0].title())
    if len(personal_items)>0:
        print("These are your saved personal items to bring to your trip: ")
        for item in personal_items:
            print('-', item[0].title())
            print(f'\nEnjoy your Trip to {city}!')

    else:
        print(f'\nEnjoy your Trip to {city}!')

    all_items = essential_items + personal_items

    return all_items


# main() # Example input: Passport, Camera, Money, Asthma medication etc.

if __name__ == '__main__':
    main()
