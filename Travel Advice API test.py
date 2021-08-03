import requests

url = "https://api.traveladviceapi.com/search/lhr:dxb"

payload={}
headers = {
  'X-Access-Token': 'ee538d1a-ffac-462e-94f3-1b3710691e29'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)