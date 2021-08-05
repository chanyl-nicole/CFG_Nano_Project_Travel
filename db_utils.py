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


def show_essential_items(month, city):
    essential_items = []
    try:
        db_name = 'travelApp'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """
        SELECT EssentialItem FROM CityWeatherByMonth as c 
        JOIN EssentialItems as e ON c.weatherType = e.weatherType  
        WHERE Month = '{month}' AND DestinationCity = '{city}' AND ItemNeeded = 1
        """.format(month=month, city=city)
        cur.execute(query)

        items = cur.fetchall()
        essential_items.append(items)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return essential_items

# print(show_essential_items())

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
