import requests
import json

url = "https://api.traveladviceapi.com/search/lhr:dxb"

payload={}
headers = {
  'X-Access-Token': 'ee538d1a-ffac-462e-94f3-1b3710691e29'
}

response = requests.request("GET", url, headers=headers, data=payload)

json_response = response.json()

masks = json_response['requirements']['masks']
quarantine = json_response['requirements']['quarantine']
tests = json_response['requirements']['tests']
origin = json_response['trips'][0]['from']
destination = json_response['trips'][0]['to']
# date = json_response['trips'][0]['start_date']

print('Masks: ', masks)
print('Quarantine: ', quarantine)
print('Tests:', tests)
print('Place of departure: ', origin)
print('Destination: ', destination)
# print('Date of trip: ', date)

###to see whole dictionary

# dictionary = json.dumps(response.json(), sort_keys = True, indent = 4)
# print(dictionary)

