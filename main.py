import requests
import json

url = "https://sandbox.travelperk.com/travelsafe/restrictions"

querystring = {"origin": "DE",
               "destination": "ES",
               "origin_type": "country_code",
               "destination_type": "country_code",
               "date": "2021-08-15"}

headers = {
    "Accept": "application/json",
    "Api-Version": "1",
    "Authorization": "ApiKey WAbFf2.zqU68TNEDYFWKkCQMZxif8gxq16A60qD",
    "Accept-Language": "en"
}

response = requests.request("GET", url, headers=headers, params=querystring)
json_response = response.json()

destination = json_response['destination']['name']
origin = json_response['origin']['name']
requirements = json_response["requirements"][0]["category"]["id"]
documents = json_response['requirements'][1]['category']['name']
to_fill = json_response['requirements'][1]['documents'][0]['document_url']


print('Destination: ', destination)
print('Origin: ', origin)
print('Requirements: ', requirements)
print('Documents: ', documents)
print('Documents needed: ', to_fill)

###to see whole dictionary

# 
# dictionary = json.dumps(response.json(), sort_keys = True, indent = 4)
# print(dictionary)

