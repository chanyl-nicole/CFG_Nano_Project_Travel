#This file was orginally used to test the different returns that we could get from the travel advice api

import requests

class UserTrip():
    def __init__(self):
        self.departure_city=" "
        self.destination = " "
        self.dep_city_airport= " "
        self.dest_city_airport= " "
        self.full_info= " " #this will be json object returned by api query
        
    

    def get_city(self):
        try:

            user_from_city = input("Enter the airport code for the airport you're flying from. e.g LHR for London Heathrow : ").capitalize()
            self.dep_city_airport = user_from_city

            user_to_city = input("Enter the airport code for the airport of your destination e.g DXB for Dubai : ").capitalize()
            self.dest_city_airport = user_to_city

        except:
          print("Please Enter A Valid Value")

        return

    def query_api(self):
        #we query api and save results as instance attibutes
        UserTrip.get_city(self)


        url = "https://api.traveladviceapi.com/search/{}:{}".format(self.dest_city_airport,self.dest_city_airport)
        payload = {}
        headers = {
          'X-Access-Token': '5f50fb53-5bca-4cc1-a2d7-7ee99a98fc8a'
        }
        # ee538d1a-ffac-462e-94f3-1b3710691e29 #orginal key

        response = requests.request("GET", url, headers=headers, data=payload)
        json_result = response.json()

        self.full_info = json_result

        city = self.full_info.get(['trips'][0])
        self.departure_city = ''.join(x for x in city[0]['from'])
        self.destination = ''.join(x for x in city[0]['to'])

        from_airport_code = ''.join(x for x in city[0]['from'].split()[-1] if x.isalnum()).lower()
        self.dep_city_airport = from_airport_code

        to_airport_code = ''.join(x for x in city[0]['to'].split()[-1] if x.isalnum()).lower()
        self.dest_city_airport = to_airport_code

    def get_restrictions(self):
        

        restrictions = self.full_info['trips'][0]['advice']['restrictions']

        for key, value in restrictions.items():
            for i, x in restrictions.get(key).items():
                print(key.upper(), ": \n{:<10} {:<10} ".format(i, x))
                

       
        return

    def get_requirements(self):

        requirements_dict = self.full_info.get('requirements')

        print(f"Requirements in {self.destination}: \n")

        for key, value in requirements_dict.items():
            print(key.upper(), ": {:<10}".format(value).capitalize())
        return

    def get_advice(self):
        try:
            date = self.full_info['start_date'][0:10]

            recommendations = '\n'.join(self.full_info.get('recommendation').split(',', 3))

            print(f'recommendation(s) for people travelling from: {self.departure_city} to: {self.destination} as of: {date} : \n {recommendations}')

        except KeyError:
            print('There is a problem with key entered')





traveller_one=UserTrip()
traveller_one.query_api()
traveller_one.get_restrictions()
traveller_one.get_requirements()
traveller_one.get_advice()
