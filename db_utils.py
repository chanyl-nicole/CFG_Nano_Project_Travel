#connect to database
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
        database=db_name
    )
    return cnx
def add_data(country,country_code,covid_pos_rate,travel_status_desc_,color,week):
    try:
        db_name = 'travelapptry'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """
            UPDATE  Country
            SET 
                `{country}` = 1, 
                `{time_id}` = '{customer}' 
            WHERE bookingDate = '{date}' AND teamMember = '{teamMember}'
            """.format(time=time, time_id=time +'-booking-id', customer=customer, date=_date, teamMember=teamMember)

        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
