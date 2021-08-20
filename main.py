### THIS MODULE REPRESENTS THE CLIENT SIDE FOR OUR TRAVEL APP
# Main function that runs our travel app is = main function at the bottom of this file

import requests, string
from db_utils import add_user_personal_items, remove_personal_items, get_country
from pprint import pprint as pp
from time import sleep


class SummerTrip:
    def __init__(self):
        self.destination = None
        self.month = None

    def get_month_choices(self):
        result = requests.get(
            'http://127.0.0.1:5001/travel/months/',
            headers={'content-type': 'application/json'}
        )
        return result.json()

    def get_cities(self):
        result = requests.get(
            'http://127.0.0.1:5001/travel/cities/',
            headers={'content-type': 'application/json'}
        )
        return result.json()

    def get_city_weather(self):
        month = self.month
        result = requests.get(
            'http://127.0.0.1:5001/travel/cities-weather-month/{}'.format(month),
            headers={'content-type': 'application/json'}
        )
        return result.json()

    def choose_month(self):
        """ This function allows the user to choose a month for
            their summer holidays and returns that month"""

        print("Are you ready to book your summer holiday? You can travel in the following months: ")
        month_choices = self.get_month_choices()
        months = []
        for month in month_choices:
            print('-', month[0])
            months.append(month[0])
        try:
            month = input("What month would you like to travel in? ").capitalize().strip()
            month = month.translate(month.maketrans("", "", string.punctuation))
            month = month.translate(month.maketrans("", "", string.digits))
            assert month in months
            self.month = month
            return self.month
        except AssertionError:
            while month not in months:
                print(f'You cannot travel in {month.title()}')
                month = input("Please choose a valid month to travel in: ").capitalize().strip()
                month = month.translate(month.maketrans("", "", string.punctuation))
                month = month.translate(month.maketrans("", "", string.digits))
                self.month = month
        finally:
            return self.month

    def choose_city(self):
        """ This function allows the user to choose a city for
        their summer holidays and returns that city"""

        month = self.month

        print("\nThe weather in the top 8 European destinations for {} is the following: ".format(month))
        city_weather = self.get_city_weather()
        for location in city_weather.keys():
            print(location, ':', '', city_weather[location])
            sleep(0.5)

        try:
            city = input("\nWhich city would you like to go to: ").title().strip()
            city = city.translate(city.maketrans("", "", string.punctuation))
            city = city.translate(city.maketrans("", "", string.digits))
            if city in city_weather.keys():
                self.destination = city
                return self.destination
            raise KeyError

        except KeyError:
            while city not in city_weather.keys():
                print(f'You cannot travel to {city.title()}')
                city = input("Please choose a valid city to travel to: ").title().strip()
                city = city.translate(city.maketrans("", "", string.punctuation))
                city = city.translate(city.maketrans("", "", string.digits))
                self.destination = city
                # return self.destination
        finally:
            return self.destination


class TripPlan(SummerTrip):
    def __init__(self):
        super().__init__()

        self.itinerary = None
        self.destination = None
        self.essentials = None
        self.restrictions = None
        self.personal_list = None

    def get_essential_items(self):
        month = self.month
        city = self.destination
        result = requests.get(
            'http://127.0.0.1:5001/travel/essential-items/{}/{}'.format(month, city),
            headers={'content-type': 'application/json'}
        )
        return result.json()

    def view_essentials(self):
        sleep(0.5)
        essential_items = self.get_essential_items()

        print("\nHere is a suggestion of essential items to bring along on your trip based on the weather: ")

        for item in essential_items:
            print('-', item[0].title())
        self.essentials = [i[0] for i in essential_items]

        return self.essentials

    def get_personal_items(self):
        result = requests.get(
            'http://127.0.0.1:5001/travel/personal-items/',
            headers={'content-type': 'application/json'}
        )
        return result.json()

    def add_personal_items(self):
        """ This function allows the user to add personal items
        needed for their holiday to the DB and returns a list of those items"""

        user_items_list = []
        counter = 0
        while counter < 10:
            user_item = input(
                "Please enter item to be saved on your personal list or enter 'done' when done: ").title().strip()
            if user_item != 'Done':
                if user_item not in user_items_list:
                    user_items_list.append(user_item)
                    add_user_personal_items(user_item)
                    print(f"{user_item} added\n")
                    counter += 1

                else:
                    print("Error! Item has already been added to the list.")
                    # user_item = input(
                    #     "\nPlease enter item to be saved on your personal list or enter 'done' when done: ").title().strip()
            elif user_item == 'Done':
                return user_items_list

    def view_personal_items(self):
        """ This function returns the personal reminder list of items """
        sleep(0.5)
        print(
            f"""\nGreat! You have selected to go to {self.destination}!\nNow you can make a list of things you would like to bring on the trip.""")
        personal_items = self.add_personal_items()

        try:
            if len(personal_items) == 0:
                raise Exception
        except:
            return self.essentials
        else:
            if len(personal_items) > 0:
                print("\nThese are your saved personal items to bring to your trip: ")
                for item in personal_items:
                    print('-', item.title())
                    self.personal_list = personal_items

                return self.personal_list

    def get_all_items(self):
        self.itinerary = self.essentials + self.personal_list
        print(
            """Here is a full list of items to bring which consists of your personal list and our suggested items: """)
        for item in self.itinerary:
            print('-', item.title())
        return self.itinerary

    def get_covid_restrictions(self):
        """This function uses the city inputted in the choose city function, then queries the database to find the
        corresponding country. Finally it queries the Travel Advice Api to return the covid restrictions for that
        country"""

        sleep(0.5)
        res = get_country(self.destination)
        res = ''.join(res[0])
        url = "https://api.traveladviceapi.com/search/{}".format(res)
        payload = {}
        headers = {
            'X-Access-Token': '1c306bba-dc9d-4f58-8b57-a3a7cf8f8ec8'  # enter API key here
        }
        #Amelia's token: 1c306bba-dc9d-4f58-8b57-a3a7cf8f8ec8
        #Sanale's new token 20/08/2021: 17615da7-3469-421f-ab80-7525426d7c3c

        response = requests.request("GET", url, headers=headers, data=payload)
        json_result = response.json()

        try:
            travelling_to = json_result['trips'][0]['to']  # country

            restrictions = json_result['trips'][0]['advice']['restrictions']

            self.restrictions = str([restrictions[i]['level_desc'].replace(',', ' ') for i in restrictions])[1:-1]

            print(f'\n Current COVID-19 restrictions in{travelling_to.replace(",", " ")}:\n ')

            for i in restrictions:
                print(i.upper().replace('_', ' '), ': \n', restrictions[i]['level_desc'].replace(',', ' '), '\n')
            return self.restrictions
        except KeyError:
            print("Key Error whilst querying API")
        else:
            return self.restrictions
    
    def clear_db(self):
        #this method clears the items in the database
        remove_personal_items()
        return
    
    def goodbye(self):

        print(f"\nEnjoy your trip to {self.destination}!")
        return


#####################   MAIN FUNCTION

def main():
    """ This function allows the user to choose a month and city for their
        summer holidays and to create a reminder list of personal items to bring to their trip
        and returns these items plus suggested essential items for the chosen destination.
        It also returns the covid restrictions for the destination country"""

    trip_one = TripPlan()
    trip_one.clear_db()
    trip_one.choose_month()
    trip_one.choose_city()
    trip_one.view_personal_items()
    trip_one.view_essentials()
    # trip_one.get_all_items()
    trip_one.get_covid_restrictions()
    trip_one.goodbye()



if __name__ == '__main__':
    main()
