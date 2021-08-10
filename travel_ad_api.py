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
# traveller_one.get_requirements()
# traveller_one.get_advice()






# risk_level = advice.get('risk_level')

#
# print("Risk level is {}".format(risk_level))
# print(requirements)
#
#
# json_example= {'id': '4a01729e-19da-4a06-84e1-4e4af9084cc0', 'name': 'Your Itinerary',
#                'start_date': '2021-08-08T19:24:01.912723512Z', 'risk_level': 'red',
#                'recommendation': 'We advise you to plan your trip taking into account restrictions in place. Also, one of the destinations in this itinerary has a containment and health index of 66%, which is an indicator of how closed the country is to travelers; a stringency index of 57% which determines how challenging it will be to move within the country, attend events, conduct business and access public transportation; and an economic support index of 50% which indicates how much was spent in countering the inpact of the pandemic on the economy.',
#                'requirements': {'tests': 'required', 'quarantine': 'depends on tests/symptoms', 'masks': 'required'},
#                'trips': [{'from': 'London, United Kingdom, (LHR)', 'to': 'Dubai, United Arab Emirates (DXB)',
#               'from_airport': 'LHR', 'to_airport': 'DXB', 'start_date': '2021-08-08T19:24:01.912723512Z',
#               'advice': {'country_code': 'AE', 'lat': '25.25', 'lon': '55.36', 'date': '2021-08-08T19:24:02.25940218Z',
#                          'level': 3, 'level_desc': 'Level 3: Ban arrivals from some regions', 'government_response_index': '64',
#                          'stringency_index': '57', 'containment_and_health_index': '66', 'economic_support_index': '50',
#                          'recommendation': 'We advise you to plan your trip taking into account restrictions in place such as international travel, circulation and public transport, schools and businesses and events and gatherings. Also, this destination has a containment and health index of 66%, which is an indicator of how closed the country is to travelers; a stringency index of 57% which determines how challenging it will be to move within the country, attend events, conduct business and access public transportation; and an economic support index of 50% which indicates how much was spent in countering the inpact of the pandemic on the economy.', 'requirements': {'tests': 'required', 'quarantine': 'depends on tests/symptoms', 'masks': 'required'}, 'restrictions': {'international_travel_controls': {'level': 3, 'level_desc': 'Level 3: Ban arrivals from some regions'}, 'restrictions_on_internal_movement': {'level': 2, 'level_desc': 'Level 2: Internal movement restrictions in place'}, 'close_public_transport': {'level': 1, 'level_desc': 'Level 1: Recommend closing (or significantly reduce volume/route/means of transport available)'}, 'stay_at_home_requirements': {'level_desc': 'Level 0: No Measures'}, 'cancel_public_events': {'level': 2, 'level_desc': 'Level 2: Require cancelling '},
#               'restrictions_on_gatherings': {'level': 4, 'level_desc': 'Level 4: Restrictions on gatherings of 10 people or less'}, 'workplace_closing': {'level': 2, 'level_desc': 'Level 2: Require closing (or work from home) for some sectors or categories of workers '}, 'school_closing': {'level': 1, 'level_desc': 'Level 1: Recommend closing'}, 'testing_policy': {'level': 3, 'level_desc': 'Level 3: Open public testing (e.g. "drive through" testing available to asymptomatic people)'}, 'contact_tracing': {'level': 2, 'level_desc': 'Level 2: Comprehensive contact tracing; done for all identified cases'}}}, 'covid19_stats': {'id': '9b25354f-4417-4321-bed3-15a5cc7870cc', 'country_iso': 'ARE', 'country': 'United Arab Emirates', 'lat': '25.25', 'lon': '55.36', 'continent': 'Asia', 'date': '2021-08-07T00:00:00Z', 'total_cases': 691554, 'new_cases': 1545, 'total_deaths': 1971, 'new_deaths': 2, 'total_cases_per_million': 69921.742, 'new_cases_per_million': 156.212, 'total_deaths_per_million': 199.284, 'new_deaths_per_million': 0.202, 'population': 9890400, 'population_density': 112.442, 'median_age': 34, 'aged_65_older': 1.144, 'aged_70_older': 0.526, 'gdp_per_capita': 67293.483, 'cvd_death_rate': 0, 'diabetes_prevalence': 17.26, 'handwashing_facilities': 0, 'hospital_beds_per_thousand': 1.2, 'life_expectancy': 77.97},
#               'data': {'containment_and_closure': {'school_closing': {'level': 1, 'level_desc': 'Level 1: Recommend closing',
#               'notes': [{'country_code': 'AE', 'type': 'school_closing', 'note': 'UAE: Ministry of Education allows the gradual return of students to schools  The Ministry of Education, in coordination with the Emirates schools establishment, announced that the gradual and phased return of regular learning is permitted for all academic levels in public schools and in the various emirates of the country, starting from February 14, 2021 until the end of the school year.  https://web.archive.org/web/20210319152758/https://gulfnews.com/uae/education/uae-ministry-of-education-allows-the-gradual-return-of-students-to-schools-1.1612332648321',
#              'sources': ['https://web.archive.org/web/20210319152758/https://gulfnews.com/uae/education/uae-ministry-of-education-allows-the-gradual-return-of-students-to-schools-1.1612332648321'], 'date': '2021-03-26T00:00:00Z'}, {'country_code': 'AE', 'type': 'school_closing', 'note': '"The Local Emergency, Crisis and Disaster Management team in Sharjah has decided 100 percent distance learning for all public and private schools in the emirate until the end of Spring Semester."   http://archive.today/7Iikw   "The decision to extend remote learning until March 25 was made to keep pupils safe, authorities said. Classroom lessons were originally suspended for at least two weeks in mid-February to curb the spread of Covid-19."  http://archive.today/cb0Zv     Schools in Dubai and Abu Dhabi are operating face to face or with the option of remote learning for parents who do not want to sent their children to school.  http://archive.today/5FSZe  ',
#             'sources': ['http://archive.today/7Iikw', 'http://archive.today/cb0Zv', 'http://archive.today/5FSZe'], 'date': '2021-02-25T00:00:00Z'},
#             {'country_code': 'AE', 'type': 'school_closing', 'note': 'Schools and universities will be allowed to open and operate from the start of the 2020/21 academic year, provided they comply with specific health and safety protocols.  Schools in Dubai differ in terms of size, location and number of students. In order to comply with health and safety guidelines, schools may choose models that best suit their circumstances and community. These can include:    Being open to all students all the time  Continuing to do distance learning part-time  Scheduling lessons in staggered ‘shifts’  Other creative solutions    We ask schools to consult with parents, teachers and students when choosing the best model for them.    https://web.archive.org/web/20210315195751/https://www.khda.gov.ae/en/safetyatschools    UAE: Ministry of Education allows the gradual return of students to schools  The Ministry of Education, in coordination with the Emirates schools establishment, announced that the gradual and phased return of regular learning is permitted for all academic levels in public schools and in the various emirates of the country, starting from February 14, 2021 until the end of the school year.    https://web.archive.org/web/20210315200526/https://gulfnews.com/uae/education/uae-ministry-of-education-allows-the-gradual-return-of-students-to-schools-1.1612332648321  ', 'sources': ['https://web.archive.org/web/20210315195751/https://www.khda.gov.ae/en/safetyatschools', 'https://web.archive.org/web/20210315200526/https://gulfnews.com/uae/education/uae-ministry-of-education-allows-the-gradual-return-of-students-to-schools-1.1612332648321'], 'date': '2021-02-14T00:00:00Z'},
#             {'country_code': 'AE', 'type': 'school_closing', 'note': 'In the emirate of Abu Dhabi, students are allowed to return to school to school from the 14th of February with the option of remote learning for parents who do not want to sent their children to school.     https://web.archive.org/web/20210214192825/https://www.arabianbusiness.com/education/458187-abu-dhabi-to-reopen-schools-on-february-14-after-approving-preventative-protocol', 'sources': ['https://web.archive.org/web/20210214192825/https://www.arabianbusiness.com/education/458187-abu-dhabi-to-reopen-schools-on-february-14-after-approving-preventative-protocol'], 'date': '2021-02-14T00:00:00Z'}]}, 'workplace_closing': {'level': 2, 'level_desc': 'Level 2: Require closing (or work from home) for some sectors or categories of workers ', 'notes': [{'country_code': 'AE', 'type': 'workplace_closing', 'note': 'Government entities and companies in Abu Dhabi can have up to 60 per cent attendance at the workplace from Sunday, May 30, the local authorities have announced.  However, on Tuesday, the Abu Dhabi Emergency, Crisis and Disasters Committee approved increasing workplace attendance to 60 per cent for all employees and outsourced workers in government entities and companies effective from Sunday.  https://web.archive.org/web/20210526103609/https://www.khaleejtimes.com/coronavirus-pandemic/covid-19-abu-dhabi-government-eases-restrictions-on-workplace-attendance', 'sources': ['https://web.archive.org/web/20210526103609/https://www.khaleejtimes.com/coronavirus-pandemic/covid-19-abu-dhabi-government-eases-restrictions-on-workplace-attendance'], 'date': '2021-05-30T00:00:00Z'},
#            {'country_code': 'AE', 'type': 'workplace_closing', 'note': '16 May, "All federal government employees will have to report to work in person from May 16." However, "The decision does not affect people employed by local government or semi-government departments...Each emirate already has separate rules for local government employees...The rules have varied for public sector workplaces across the country. In Abu Dhabi, local and \'semi-government entities\' remain at 30 per cent, as do many private sector workplaces."    As such, I am keeping the coding as 2T.     Source: https://archive.vn/WamFT  https://archive.vn/19IGE  https://archive.vn/WWpDb  https://archive.vn/UriE3', 'sources': ['https://archive.vn/WamFT', 'https://archive.vn/19IGE', 'https://archive.vn/WWpDb', 'https://archive.vn/UriE3'], 'date': '2021-05-16T00:00:00Z'}, {'country_code': 'AE', 'type': 'workplace_closing', 'note': 'In Dubai, "Restaurants and cafes will continue to close by 1.00 am; pubs/bars to remain closed."   https://archive.vn/QrVYd  Workplaces continue to operate at a reduced capacity with closure of some entertainment facilities.   https://web.archive.org/web/20210214195422/https://www.thenationalnews.com/uae/government/abu-dhabi-government-to-cut-workplace-attendance-to-30-per-cent-1.1160679  All government employees in Sharjah are working from home.   https://archive.vn/pZsqH', 'sources': ['https://archive.vn/QrVYd', 'https://web.archive.org/web/20210214195422/https://www.thenationalnews.com/uae/government/abu-dhabi-government-to-cut-workplace-attendance-to-30-per-cent-1.1160679', 'https://archive.vn/pZsqH'], 'date': '2021-02-27T00:00:00Z'},
#             {'country_code': 'AE', 'type': 'workplace_closing',  'note': 'No change in policy  https://web.archive.org/web/20210214195422/https://www.thenationalnews.com/uae/government/abu-dhabi-government-to-cut-workplace-attendance-to-30-per-cent-1.1160679   https://archive.vn/XaXS3 ', 'sources': ['https://web.archive.org/web/20210214195422/https://www.thenationalnews.com/uae/government/abu-dhabi-government-to-cut-workplace-attendance-to-30-per-cent-1.1160679', 'https://archive.vn/XaXS3'], 'date': '2021-02-23T00:00:00Z'}]}, 'cancel_public_events': {'level': 2, 'level_desc': 'Level 2: Require cancelling ', 'notes': [{'country_code': 'AE', 'type': 'cancel_public_events', 'note': 'While Dubai lifted many restrictions on 17 May, including "lifted a series of restrictions on live entertainment and hotel occupancy and permitted concerts for vaccinated people," other emirates have still continued to ban and limit public events. As such, 2T coding will remain.   https://archive.vn/4P9iT  https://web.archive.org/web/20210517165328/https://www.thenationalnews.com/uae/government/dubai-covid-19-rules-overhaul-allows-concerts-10-diners-to-a-table-and-weddings-for-100-1.1224217    ', 'sources': ['https://archive.vn/4P9iT', 'https://web.archive.org/web/20210517165328/https://www.thenationalnews.com/uae/government/dubai-covid-19-rules-overhaul-allows-concerts-10-diners-to-a-table-and-weddings-for-100-1.1224217'], 'date': '2021-05-17T00:00:00Z'}]}, 'restrictions_on_gatherings': {'level': 99}, 'close_public_transport': {'level_desc': 'Level 0: No Measures', 'notes': [{'country_code': 'AE', 'type': 'close_public_transport', 'note': 'Level 0: No Measures', 'sources': None, 'date': '2021-02-14T00:00:00Z'}, {'country_code': 'AE', 'type': 'close_public_transport', 'note': 'Level 0: No Measures', 'sources': None, 'date': '2021-02-13T00:00:00Z'},
#

#
# user_from_city = input("Enter City of Departure: ").capitalize()
#
# user_to_city = input("Enter Destination City: ").capitalize()
# city = json_example.get(['trips'][0])
# travel_restrictions_level = json_example['trips'][0]['advice']['level_desc']
#
# restrictions = json_example['trips'][0]['advice']['restrictions']
#
# for key, value in restrictions.items():
#     for i, x in restrictions.get(key).items():
#         print(key.upper(), ": \n{:<10} {:<10} ".format(i, x))




#
#
#
# from_city= ''.join(x for x in city[0]['from'])
# to_city= ''.join(x for x in city[0]['to'])
# from_airport_code = ''.join(x for x in city[0]['from'].split()[-1] if x.isalnum()).lower()
#
# to_airport_code = ''.join(x for x in city[0]['to'].split()[-1] if x.isalnum()).lower()
# requirements_dict= json_example.get('requirements')
# recommendations = '\n'.join(json_example.get('recommendation').split(',',3))
#
#
# print(from_city,to_city,from_airport_code,to_airport_code,f'recommendation(s) for travelling to {to_city} : \n {recommendations}')
# print(f'Requirements for people travelling to {to_city}: \n ')
# for key,value in requirements_dict.items():
#
#     print(key.upper(), ": {:<10}".format(value).capitalize())




# masks = json_example['requirements']['masks','quarantine,tests']
# quarantine = json_example['requirements']['quarantine']
# tests = json_example['requirements']['tests']
