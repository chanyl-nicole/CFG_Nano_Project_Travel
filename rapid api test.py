import requests
from pprint import pprint as pp

url = "https://eu-covid-19-travel.p.rapidapi.com/travel/Austria"
headers = {
    'x-rapidapi-key': "8f2d1ce8camshbb877147abb08d0p1ad81ajsn974176ee9873",
    'x-rapidapi-host': "eu-covid-19-travel.p.rapidapi.com"
    }
response = requests.request("GET", url, headers=headers)
pp(response.text)

