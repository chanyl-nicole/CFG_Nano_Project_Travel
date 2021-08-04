import mysql.connector
from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database= db_name
    )
    return cnx

### weather type and desitnation cities are placeholders and can change the type in cur.execute query
### These should be updated depending on user inputs - but how?

def show_essential_items():
    essential_items = []
    try:
        db_name = 'travelApp'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """
        SELECT EssentialItem FROM CityWeatherByMonth as c 
        JOIN EssentialItems as e ON c.weatherType = e.weatherType  
        WHERE Month = %s AND DestinationCity = %s AND ItemNeeded = 1
        """
        cur.execute(query, ('August', 'London', ))

        items = cur.fetchall()
        essential_items.append(items)
        # for essential_item in essential_items:
        #     print(essential_item)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return essential_items

print(show_essential_items())

def show_cities():
    places = []
    try:
        db_name = 'travelApp'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = "SELECT DISTINCT DestinationCity FROM CityWeatherByMonth"
        cur.execute(query)

        cities = cur.fetchall()
        places.append(cities)
        # print(places)
        # for city in cities:
        #     print(city)

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return places

# show_cities():

def show_months():
    months = []
    try:
        db_name = 'travelApp'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = "SELECT DISTINCT Month FROM CityWeatherByMonth"
        cur.execute(query)

        month = cur.fetchall()
        # for month in months:
        #     print(month)
        month.append(months)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return month

# print(show_months())


### I don't think the below  is needed

# def show_essential_items_two():
#     essential_items = []
#     try:
#         db_name = 'travelApp'
#         db_connection = _connect_to_db(db_name)
#         cur = db_connection.cursor()
#         print("Connected to DB: %s" % db_name)
#
#         query = "SELECT EssentialItem FROM EssentialItems WHERE WeatherType = %s and ItemNeeded = 1"
#         cur.execute(query,('DryWarm', ) )
#
#         items = cur.fetchall()
#         essential_items.append(items)
#         # for essential_item in essential_items:
#         #     print(essential_item)
#         cur.close()
#
#     except Exception:
#         raise DbConnectionError("Failed to read data from DB")
#
#     finally:
#         if db_connection:
#             db_connection.close()
#             print("DB connection is closed")
#
#     return essential_items
#
# # print(show_essential_items())