import requests
from flask import render_template
import json

destinations= ["Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland",
               "France", "Germany", "Greece", "Hungary", "Ireland", "Italy",
               "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovakia",
               "Slovenia", "Spain", "Sweden"]


def get_travel_status():
    try:
        user_input= input("Where do you want to go?: ")
        if user_input in destinations:
            url = "https://eu-covid-19-travel.p.rapidapi.com/travel/{}".format(user_input)
            headers = {
                'x-rapidapi-key': "8f2d1ce8camshbb877147abb08d0p1ad81ajsn974176ee9873",
                'x-rapidapi-host': "eu-covid-19-travel.p.rapidapi.com"
            }
            response = requests.request("GET", url, headers=headers)
            y = response.json()

            print("Travel status for {} is : {}".format(user_input,y[0]['travel_status']))
    except ValueError:
        print("Please Enter Valid EU Country")


get_travel_status()




