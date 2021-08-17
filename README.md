########## CFG_Nano_Project_Travel

##### App name

TravelApp

##### About TravelApp

TravelApp is an application developed to help the user plan their summer holidays. 

TravelApp functions in the following manner: initially, it asks the user in which summer month (June, July, August or September) they would like to travel in. Then, the app provides the top 8 European holiday destinations and the expected weather in those locations for that month. With this information, the user now makes a choice of the city they would like to travel to. After this, the app allows the user to input up to ten personal items to bring to their trip that will be stored in a 'remainder list'. Finally, the app returns a list of essential suggested items for the user to bring to their holidays (according to the expected weather on the destination of choice) and it also shows the personal items previously added by the user to the remainder list.

Notes:

	Top 8 holiday destinations in Europe: Paris, London, Rome, Florence, Barcelona, Swiss Alps, Amsterdam, Santorini.
	
	The app considers warm weather that with average monthly maximum temperature = or > 15C and cold weather that with average monthly maximum temperature < 15C.
	
	The app considers wet weather that with average monthly average rainfall = > 50 mm and dry weather that with average monthly average rainfall  < 50 mm.
	
	This information was obtained from Google weather graphs and used to classify the weather expected in each city for each month accordingly on our database.
	
	The essential travel items for each weather type were obtained after searching several blogs and websites with information on the matter.


##### Tools and packages needed to run TravelApp

In order to run TravelApp, the following tools/packages must be pre-installed:

	1) mysql-connector Python library
	

##### App files

1) create_travelApp_db_script.sql
2) config.py
3) db_utils.py
4) app.py
5) main.py
6)  ....................testing ..............................

Here is a brief description of their functions:

1) create_travelApp_db_script.sql: 

	- sql script that builds the database for the app. It generates the following tables i) 'CityWeatherByMonth', in which each entry refers to a month, a city and the expected weather for that city during that month; ii) 'EssentialItems' in which each entry refers to an essential item, weather type and if the item is needed or not for that weather type and; iii) 'MyEssentials', which is an empty table that will be populated with items inputted by the user.

2) config.py:

	- Contains the 'host' name, 'user' name and 'password' stored as variables needed to be used by the function that establishes a connection with the sql database. This function is defined in the module db_utils.py.


3) db_utils.py:

	- This module contains the functions needed for establishing a connection to the database, querying the database and adding data to it. The functions on it do the following: i) retrieve data on the summer months in which the user can choose to travel; ii) retrieve the expected weather type for the top 8 European destinations for the chosen month; iii) retrieve the essential items needed for travelling in that type of weather. It also contains a function that iv) allows the app to insert data on the database table for personal essential items for the trip (to be inputed by the user); and another function that v) deletes the data on this last table so the table is emptied before the app is run again.

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
		 
	- The module also contains a set of helper functions that are finally invoked by the main function of the app. This function is called plan_your_trip(). 


6)  ....................testing ..............................

##### Instructions on how to run the app

1) Make sure that mysql-connector Python library is pip installed in your working environment
2)
3) run app.py module to generate endpoints
4) run main.py module

	- This runs the main function main(): it allows the user to chose a month for their holidays, then, returns the expected weather for that month in the 8 proposed destinations, then, it allows the user to chose their destination. After that, the user is prompted to input up to 10 personal items that they would want to be reminded off to bring to their trip. Finally, it gives back a list of essential suggested items for the trip plus the personal items inputted by the user. For this, follow the set of instructions below (point 4).
	
5) Follow instructions prompted in the python console:
	Select the summer month you would like to travel in.
	Select the city you would like to travel too.
	Add personal items you would like to be reminded of to bring to your trip. You can add up to 10 items or just type 'done' if you don't have more items to add.
	You now will get the suggested essential items plus your saved personal items to bring to your trip.

6)  ....................testing ..............................
	- In order to run the testing module................

	
	
Requests to the Travel Advice Api are limited to 100 per account on the free version. If you experience an authentication error for this then it may be that the limit has been reached. If this is the case please sign up for a free account at https://app.traveladviceapi.com/sign-up  to generate a new api key. Once you have received your key please insert into the string fields into line 152 of the Main.py file. (replace the existing key).
