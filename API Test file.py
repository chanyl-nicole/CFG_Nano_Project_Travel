
url = "https://sandbox.travelperk.com/travelsafe/restrictions"

origin_code= input("Enter 2 digit country code you are travelling from").upper() #this needs to be DE
destination_code = input("Enter 2 digit country code you are travelling to").upper() #this needs to be ES

querystring = {"origin": "{}".format(origin_code),
               "destination": "{}".format(destination_code),
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
travel_status = json_response['authorization_status']
requirements = json_response['summary']
quarantine = json_response['requirements'][0]['summary']
documents = json_response['requirements'][1]['category']['name']
to_fill = json_response['requirements'][1]['documents'][0]['document_url']


print('Origin: ', origin)
print('Destination: ', destination)
print('Travel Status: ',travel_status)
print('Requirements: ', requirements)
print('Quarantine: ', quarantine)
# print('Documents: ', documents)
print('Documents needed prior to arrival: ', to_fill)

###to see whole dictionary

#
# dictionary = json.dumps(response.json(), sort_keys = True, indent = 4)
# print(dictionary)

