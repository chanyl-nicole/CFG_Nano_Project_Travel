### THIS MODULE REPRESENTS THE CLIENT SIDE FOR OUR TRAVEL APP

# This is the code acting in the 'frontend'
# Main function that runs our travel app is = main function at the bottom of this file

import requests,string
from db_utils import add_user_personal_items, remove_personal_items,get_country
from pprint import pprint as pp

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
        # test = get_month_choices()
        # pp(test)
        #[['August'], ['July'], ['June'], ['September']]
    
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
        # print(months)
        try:
            month = input("What month would you like to travel in? ").capitalize().strip()
            month = month.translate(month.maketrans("", "", string.punctuation))
            month = month.translate(month.maketrans("", "", string.digits))
            assert month in months
            self.month=month
            return self.month
        except AssertionError:
            while month not in months:
                print(f'You cannot travel in {month.title()}')
                month = input("Please choose a valid month to travel in: ").capitalize().strip()
                month = month.translate(month.maketrans("", "", string.punctuation))
                month = month.translate(month.maketrans("", "", string.digits))

        finally:
            return self.month
            



    def choose_city(self):
        """ This function allows the user to choose a city for
        their summer holidays and returns that city"""
        
        month= self.month

        print("\nThe weather in the top 8 European destinations for {} is the following: ".format(month))
        city_weather = self.get_city_weather()
        for location in city_weather.keys():
            print(location, ':', '', city_weather[location])
        
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

        finally:
            return self.destination

        # IMPORTANT for DEBUGGING AND TESTING:
        # here, if input is not a valid city, should raise an Exception!!!!
        # also, good case for testing what happens if we give the right or wrong input!
        """ This function allows the user to choose a city for
        their summer holidays and returns that city"""


    # choose_city('June')


class TripPlan(SummerTrip):
    def __init__(self):
        super().__init__()
        
        self.itinerary= None
        self.destination= None
        self.essentials = None
        self.restrictions = None
        self.itinerary = None
        

    def get_essential_items(self):
        month = self.month
        city= self.destination
        result = requests.get(
            'http://127.0.0.1:5001/travel/essential-items/{}/{}'.format(month, city),
            headers={'content-type': 'application/json'}
        )
        return result.json()

         # test = get_essential_items('June', 'Paris')
         # pp(test)
    
    def view_essentials(self):
        essential_items = self.get_essential_items()
        
        print("\nHere is a suggestion of essential items to bring along on your trip based on the weather: ")
        
        for item in essential_items:
            print('-', item[0].title())
        self.essentials = essential_items

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
            user_item = input("Please enter item to be saved on your personal list or enter 'done' when done: ").capitalize().strip()
            if user_item != 'Done':
                user_items_list=[]
        
                if user_item not in user_items_list:
                    user_items_list.append(user_item)
                    add_user_personal_items(user_item)
                    counter += 1
                                    
        else:
            return user_items_list
    

        #add_personal_items()
        # test = get_personal_items()
        # pp(test)

    def view_personal_items(self):
        personal_items= self.add_personal_items()
        
        try:
            if len(personal_items) == 0:
                raise Exception
        except:
            return self.essentials
        else:
            if len(personal_items) > 0:
                print("These are your saved personal items to bring to your trip: ")
                for item in personal_items:
                    print('-', item.capitalize())
                self.itinerary = personal_items

                return self.itinerary


    def get_covid_restrictions(self):
        
        res = get_country(self.destination)
        res= ''.join(res[0])
        url = "https://api.traveladviceapi.com/search/{}".format(res)
        payload = {}
        headers = {
            'X-Access-Token': '01871f9a-1d26-469b-b7fb-7c49e4c6bac4'
        }
        # ee538d1a-ffac-462e-94f3-1b3710691e29 #orginal key

        response = requests.request("GET", url, headers=headers, data=payload)
        json_result = response.json()
        
        try:
            travelling_to = json_result['trips'][0]['to'] #country
        
            restrictions = json_result['trips'][0]['advice']['restrictions']
            
            self.restrictions=str([restrictions[i]['level_desc'].replace(',',' ')for i in restrictions])[1:-1]
            
        
            print(f'\n Current COVID-19 restrictions in {travelling_to.replace(","," ")}:\n ')
        
            for i in restrictions:
                print(i.upper().replace('_',' '), ': \n',restrictions[i]['level_desc'].replace(',',' '),'\n') 
        except KeyError:
            print("Key Error whilst querying API")
        else:
            
            return self.restrictions
        
        

#####################   MAIN FUNCTION

def main():
    """ This function allows the user to choose a month and city for their
        summer holidays and to create a remainder list of personal items to bring to their trip
        and returns these items plus suggested essential items for the chosen destination"""

    trip_one= TripPlan()
    trip_one.choose_month()
    trip_one.choose_city()
    trip_one.view_personal_items()
    trip_one.view_essentials()
    trip_one.get_covid_restrictions()
   


if __name__ == '__main__':
    main()
