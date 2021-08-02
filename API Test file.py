import requests
from pprint import pprint as pp

url = "https://sandbox.travelperk.com/travelsafe/restrictions"

querystring = {
    "origin":"DE",
    "destination":"ES",
    "origin_type":"country_code",
    "destination_type":"country_code",
    "date":"2020-10-15"
}

headers = {
    "Api-Version": "1",
    "Authorization": "Apikey WAbFf2.zqU68TNEDYFWKkCQMZxif8gxq16A60qD"
}

response = requests.request("GET", url, headers=headers, params=querystring)

pp(response.text)

