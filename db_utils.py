import mysql.connector
from mysql.connector.errors import InterfaceError
from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


def _connect_to_db(db_name):
    """ This function connects python to our database"""
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


def show_essential_items(month, city):
    """ This function returns a list of essential items for your trip"""
    try:
        db_name = 'travelApp'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        # print("Connected to DB: %s" % db_name)

        query = """
        SELECT Item,Weather_type,City, Month FROM Essential_Items as e

        JOIN Weather AS w ON e.Suitable_weather = w.weather_type_id
        JOIN city as c on c.weather_type_id = w.weather_type_id
        JOIN Months as m on c.month_id= m.month_id
        WHERE Month = '{month}' AND city = '{city}'
        """.format(month=month, city=city)
        cur.execute(query)

        essential_items = cur.fetchall()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            # print("DB connection is closed")

    return essential_items


# items = show_essential_items('August', 'Barcelona')
# print(items)

def get_country(city):
    try:
        db_name = 'travelApp'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()

        # print("Connected to DB: %s" % db_name)

        query = """
                    SELECT DISTINCT Country FROM Country  as cnt
                    JOIN City as c ON c.Country_id =cnt.country_id
                    where c.city= '{}'
                   """.format(city)

        cur.execute(query)

        country = cur.fetchall()

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            # print("DB connection is closed")
    return country


x= get_country('London')
''.join(x[0])


def show_cities():
    """ This function returns a list of the top 8 european holiday destinations"""
    try:
        db_name = 'travelApp'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        # print("Connected to DB: %s" % db_name)

        query = "SELECT DISTINCT City FROM City"
        cur.execute(query)

        cities = cur.fetchall()

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            # print("DB connection is closed")

    return cities


# show_cities()
# print(show_cities())

def show_months():
    """ This function returns a list of the summer months in which
    the user can book a summer holiday"""
    try:
        db_name = 'travelApp'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        # print("Connected to DB: %s" % db_name)

        query = "SELECT month FROM Months"
        cur.execute(query)

        months = cur.fetchall()

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            # print("DB connection is closed")

    return months


# show_months()
# print(show_months())


def show_cities_and_weather(month):
    """This function returns a dictionary with cities as keys and expected weather as
    values for a specific month"""
    try:
        db_name = 'travelApp'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        # print("Connected to DB: %s" % db_name)

        query = """
        SELECT City, Weather_type from City as c
        JOIN Weather as w on c.weather_type_id = w.weather_type_id
        JOIN Months as m on m.month_id = c.month_id
        WHERE m.Month = '{month}' """.format(month=month)
        cur.execute(query)

        city_and_weather = cur.fetchall()
        cur.close()

        cities_weather = {}
        for pair in city_and_weather:
            cities_weather[pair[0]] = pair[1]

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            # print("DB connection is closed")

    return cities_weather


# print(show_cities_and_weather('August'))

def add_user_personal_items(user_item):
    """ This function adds personal items inputted by the user
     to a table of essential personal items for travelling on the DB"""
    try:
        db_name = 'travelApp'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        # print("Connected to DB: %s" % db_name)

        query = """INSERT INTO My_Essentials (MyEssentialItem)
         VALUES ('{}')""".format(user_item)

        cur.execute(query)
        db_connection.commit()
        cur.close()
    except In:
        InterfaceError("This item already exists in list.")

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            # print("DB connection is closed")

    print("Personal item added")  # print("Personal item added to DB")


# add_user_personal_items('raincoat')

def show_personal_items():
    """ This function returns a list of personal items needed for travelling
        previously stored in the DB by the user"""
    try:
        db_name = 'travelApp'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        # print("Connected to DB: %s" % db_name)

        query = "SELECT MyEssentialItem FROM My_Essentials"
        cur.execute(query)

        personal_items = cur.fetchall()

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            # print("DB connection is closed")

    return personal_items


# show_personal_items()
# print(show_personal_items())

def remove_personal_items():
    """ This function clears the table storing personal items
    inputted by the user in the DB """
    try:
        db_name = 'travelApp'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        # print("Connected to DB: %s" % db_name)

        query = """DELETE FROM My_Essentials WHERE (MyEssentialItem) IS NOT NULL"""

        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            # print("DB connection is closed")

    # print("Personal items removed from DB")

# remove_personal_items()

#####

## I don't think we will use this function below for now (or at all), we will see

# def show_weather():
#     try:
#         db_name = 'travelApp'
#         db_connection = _connect_to_db(db_name)
#         cur = db_connection.cursor()
#         print("Connected to DB: %s" % db_name)
#
#         query = "SELECT DISTINCT WeatherType FROM CityWeatherByMonth"
#         cur.execute(query)
#         weather = cur.fetchall()
#
#         cur.close()

