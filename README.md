########## CFG_Nano_Project_Travel

##### App name

TravelApp

##### About TravelApp

TravelApp is an application developed to help the user plan their summer holidays.

TravelApp functions in the following manner: initially, it asks the user in which summer month (June, July, August or September) they would like to travel in. Then, the app provides the top 8 European holiday city destinations (Paris, London, Rome, Florence, Barcelona, Swiss Alps, Amsterdam or Santorini) and the expected weather in those locations for the month of travel. With this information, the user can make a choice of the city they would like to travel to. After this, the app allows the user to input up to ten personal items to bring on their trip and these will be stored in a personal 'reminder list'. The app then returns a list of suggested essential items for the user to bring on their holidays (according to the expected weather on the destination of choice) and it also shows the personal items previously added by the user to the reminder list. The app finally returns the Covid-related restrictions for the country in which the destination city is situated.

Notes:

	Top 8 holiday destinations in Europe: Paris, London, Rome, Florence, Barcelona, Swiss Alps, Amsterdam, Santorini.
	
	The app considers warm weather that with average monthly maximum temperature = or > 15C and cold weather that with average monthly maximum temperature < 15C.
	
	The app considers wet weather that with average monthly average rainfall = > 50 mm and dry weather that with average monthly average rainfall  < 50 mm.
	
	This information was obtained from Google weather graphs and used to classify the weather expected in each city for each month accordingly in our database.
	
	The essential travel items for each weather type were obtained after searching several blogs and websites with information on this matter.
	
	The country Covid-related restrictions are obtained by the app querying Travel Advice API.


##### Tools and packages needed to run TravelApp

In order to run TravelApp, the following tools/packages must be pre-installed:

	1) mysql-connector Python library

In order run the tests created for the functions in the main.py module, the following command must be run on the terminal:

	python3 -m unittest tests.py


##### App files

1) travel_app_db.sql
2) config.py
3) db_utils.py
4) app.py
5) main.py
6) tests.py

Here is a brief description of their functions:


1) travel_app_db.sql:

	- sql script that builds the database for the app. It generates several tables: 
	
	i) 'Country', where each entry refers to a country in which the top destinations are located and these are given unique ids;
	ii) 'Months', where each entry refers to a summer month and these are given unique ids; 	
	iii) 'Weather', where each entry refers to a weather type and these are given unique ids; 
	iv) 'Essential_items', where each entry refers to an essential item and the weather type for which that item is suggested as essential;
	v) 'City', where each entry refers to a city, it's country, each summer month and the expected weather for that city during that month;
	vi) 'My_Essentials', which is an empty table that will be populated with items inputted by the user whilst running the travel app.

2) config.py:

	- Contains the 'host' name, 'user' name and 'password' stored as variables needed to be used by the function that establishes a connection with the sql database. 
	****N.B the user needs to enter their mysql password into the string field in line 3 of this file, otherwise will fail to connect to the database.****
	- This function is defined in the module db_utils.py.

3) db_utils.py:

	- This module contains the functions needed for establishing a connection to the database, querying the database and adding data to it. 
	- The functions in this file do the following: 
	i) retrieve data on the summer months in which the user can choose to travel; 
	ii) retrieve the expected weather type for the top 8 European destinations for the chosen month; 
	iii) retrieve the essential items needed for travelling in that type of weather;
	iv) allow the app to insert data on the database table for personal essential items for the trip (to be inputed by the user); 
	v) delete the data on this last table so the table is emptied before the app is run again. 

4) app.py:

	- This module defines the app functionality. The functions it contains get data from the database (based on the functions previously defined in db-utils.py) and publish these data on specific urls in json format. They generate the endpoints at specific urls. For example, an endpoint will be generated showing the expected weather type for each city on an specific month etc. 
	
	Example:
	
	@app.route('/travel/cities-weather-month/<month>', methods=['GET'])
	def app_get_city_weather(month):
	    res = show_cities_and_weather(month)
    	    return jsonify(res)
	    
	 Example output = 
	    
	    http://127.0.0.1:5001/travel/cities-weather-month/month

5) main.py:

	- This module represents the 'client side' for our travel app and contains the code acting at the 'front end'. The module contains a set of functions that allow making requests to the endpoints previously generated with the app module. 
	
	For example, the function below makes a request that gets back the expected weather for each city for an specific month that will be selected by the user.

	def get_city_weather(month):
    		result = requests.get(
        			'http://127.0.0.1:5001/travel/cities-weather-month/{}'.format(month),
        			headers={'content-type': 'application/json'}
   		 )
   		 return result.json()
		 
	- The module also contains a set of helper functions that are finally invoked by the main function of the app, including a function to retrieve Covid-related restrictions per country (by querying the Travel Advice API). The main function in this module is called main().

6) tests.py:

	- This file can be run to test that the functions on main.py work as expected.
	- **** In order run the tests created for the functions in the main.py module, the following command must be run on the terminal:
	python3 -m unittest tests.py****


##### Instructions on how to run the app

1) Make sure that mysql-connector Python library is pip installed in your working environment.
2) Replace the word "password" in the line 3 of the config.py file with your own mysql password.
3) Run app.py module to generate endpoints.
4) Run main.py module (whilst app.py is also running):

	- This runs the main function main(). This function allows the user to chose a month for their holidays, then, returns the expected weather for that month in the 8 top European holiday destinations. It then allows the user to chose their destination. After that, the user is prompted to input up to 10 personal items that they would want to be reminded of to bring on their trip. Finally, the app gives back a list of essential suggested items for the trip plus the personal items inputted by the user. The app finally returns the Covid-related restrictions for the country in which the destination city is situated. For this, follow the set of instructions below (point 5).
	
5) Follow instructions prompted in the python console when running main.py:
	- Select the summer month you would like to travel in.
	- Select the city you would like to travel too.
	- Add personal items you would like to be reminded of to bring to your trip. You can add up to 10 items or just type 'done' if you don't have more items to add.
	- You now will get the suggested essential items and your saved personal items to bring to your trip.

IMPORTANT NOTE:

Requests to the Travel Advice Api are limited to 100 per account on the free version. If you experience an authentication error for this then it may be that the limit has been reached. If this is the case please sign up for a free account at https://app.traveladviceapi.com/sign-up to generate a new api key. Once you have received your key please insert into the string fields into line 204 of the Main.py file. (Replace the existing key).
