#App file to define app routes

from flask import Flask, jsonify

from db_utils import (get_country, show_cities, show_cities_and_weather,
                      show_essential_items, show_months, show_personal_items)

app = Flask(__name__)

@app.route('/travel/months/', methods=['GET'])
def app_get_month_choices():
    res = show_months()
    return jsonify(res)

    # Generates this URL =
        #http://127.0.0.1:5001/travel/months/


##  GET TOP 8 EUROPEAN DESTINATIONS FOR SUMMER HOLIDAYS
@app.route('/travel/cities/', methods=['GET'])
def app_get_cities():
    res = show_cities()
    return jsonify(res)

    #http://127.0.0.1:5001/travel/cities/


##  GET WEATHER FOR TOP 8 EUROPEAN DESTINATIONS FOR SELECTED MONTH
@app.route('/travel/cities-weather-month/<month>', methods=['GET'])
def app_get_city_weather(month):
    res = show_cities_and_weather(month)
    return jsonify(res)

    #http://127.0.0.1:5001/travel/cities-weather-month/

    # Example: http://127.0.0.1:5001/travel/cities-weather-month/July


##  GET ESSENTIAL ITEMS FOR SELECTED MONTH AND DESTINATION
@app.route('/travel/essential-items/<month>/<city>', methods=['GET'])  # generates the endpoint at an specific URl
def app_get_essential_items(month, city):
    res = show_essential_items(month, city)
    return jsonify(res)

    # http://127.0.0.1:5001/travel/essential-items/month/city
    # Example: http://127.0.0.1:5001/travel/essential-items/July/Paris



# GET PERSONAL ITEMS NEEDED FOR TRIP
@app.route('/travel/personal-items/', methods=['GET'])
def app_get_personal_items():
    res = show_personal_items()
    return jsonify(res)

    #http://127.0.0.1:5001/travel/personal-items/



if __name__ == '__main__':
    app.run(debug=True, port=5001)
