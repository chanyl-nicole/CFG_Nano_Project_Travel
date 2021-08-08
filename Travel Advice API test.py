import requests

from_airport = input("Enter 3 digit code of airport flying from").upper()
to_airport = input("Enter 3 digit code of airport flying to").upper()

url = "https://api.traveladviceapi.com/search/{}:{}".format(from_airport,to_airport)


payload={}
headers = {
  'X-Access-Token': '#insert own key here'
}
#ee538d1a-ffac-462e-94f3-1b3710691e29 #orginal key

response = requests.request("GET", url, headers=headers, data=payload)
advice = response.json()

# origin = advice['trips']['from'] #can't get this dictionary to work
# destination = advice['trips']['to']


risk_level = advice['risk_level']
requirements = advice['requirements']



print("Risk level is {}".format(risk_level))
print(requirements)
print(origin)