######### CFG_Nano_Project_Travel
​
## App name
​
TravelApp
​
## About TravelApp
​
TravelApp is an application developed to help the user plan their summer holidays. 
​
TravelApp functions in the following manner: initially, it asks the user in which summer month (June, July, August or September) they will like to travel on. Then, the app provides the top 8 European holiday destinations and the expected weather in destination location for that month. With this information, user now makes a choice of the city they will like to travel to. After this, the app allows the user to input up to ten personal items to bring to their trip that will be stored in a 'remainder list'. Finally, the app returns a list of essential suggested items for the user to bring to their holidays (according to the expected weather on the destination of choice) and it also shows the personal items previously added by the user to the remainder list.
​
Notes:
​
	Top 8 destinations in Europe: Paris, London, Rome, Florence, Barcelona, Swiss Alps, Amsterdam, Santorini.
	
	The app considers warm weather that with average monthly maximum temperature = or > 15C and cold weather that with average monthly maximum temperature <15C.
	
	The app considers wet weather that with average monthly average rainfall = > 50 mm and dry weather that with average monthly average rainfall  < 50 mm.
	
	This information was obtained from Google weather graphs and used to classify the weather of each city per month accordingly on the database.
	
	The essential travel items for each weather type were 
​
## Packages needed to run TravelApp
​
In order to run TravelApp, the following packages must be pre-installed:
​
	1) mysql-connector Python library
	
​
## App files
​
1) create_travelApp_db_script.sql
2) config.py
3) db_utils.py
4) app.py
5) main.py
​
Here is a brief description of their functions:
​
1) create_travelApp_db_script.sql: sql script that builds the database for the app. It generates the following tables i) 'CityWeatherByMonth', in which it entry refers to a month, a city and the expected weather for that city during that month; ii) 'EssentialItems' in which it entry refers to an essential item, weather type and if the item is needed or not for that weather and; iii) 'MyEssential', which is an empty table that will be populated with items inputted by the user.
​
2) config.py:
​
​
3) db_utils.py:
​
establishes a connection to the database
​
​
4) app.py:
​
5) main.py:
​
​
## Instructions on how to run the app
​
1) Make sure that mysql-connector Python library is pip installed in your working environment
2) run app.py file to create endpoints
3) run main.py
4) Follow instructions prompted in the python console:
	Select the summer month you would like to travel in
	Select the 





