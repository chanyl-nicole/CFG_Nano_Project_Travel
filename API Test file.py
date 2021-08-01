import requests

url = "https://api.travelperk.com/travelsafe/restrictions"

querystring = {
    "origin":"FR",
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

print(response.text)

