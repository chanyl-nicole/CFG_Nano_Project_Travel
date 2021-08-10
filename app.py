from flask import Flask, jsonify, request

from db_utils import show_essential_items, show_months, show_cities, show_cities_and_weather, show_personal_items

app = Flask(__name__)

#  GET MONTHS FOR SUMMER HOLIDAYS
    # get data from DB, put in json format, publish in the specified place (URL)
    @app.route('/travel/<months>')  # generates the endpoint at an specific URl
    def app_get_month_choices(): # better rename=  def get_months()
        res = show_months()
        return jsonify(res)

#  GET TOP 8 EUROPEAN DESTINATIONS FOR SUMMER HOLIDAYS
    @app.route('/travel/<cities>')
    def app_get_cities():
        res = show_cities()
        return jsonify(res)

#  GET WEATHER FOR TOP 8 EUROPEAN DESTINATIONS FOR SELECTED MONTH
    @app.route('/travel/<cities-weather-month>')
    def app_get_city_weather(month): # better rename=  def get_city_weather()
        res = show_cities_and_weather(month)
        return jsonify(res)

#  POST LIST OF PERSONAL ITEMS NEEDED FOR TRIP -  not sure how to do this!

    #add_user_personal_items(user_item)

#  GET ESSENTIAL ITEMS FOR SELECTED MONTH AND DESTINATION
    @app.route('/travel/<essential-items>')  # generates the endpoint at an specific URl
    def app_get_essential_items(month, city):
        res = show_essential_items(month, city)
        return jsonify(res)

#  GET PERSONAL ITEMS NEEDED FOR TRIP
    @app.route('/travel/<personal-items>')
    def app_get_personal_items(): # better rename=  def get_personal_items()
        res = show_personal_items()
        return jsonify(res)

#  GET ALL ITEMS TO BRING TO OUR HOLIDAYS?

#  GET COVID INFO FOR DESTINATION?


if __name__ == '__main__':
    app.run(debug=True, port=5001)
