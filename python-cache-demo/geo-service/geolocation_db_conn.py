import mysql.connector
import logging

class GeolocationDBConnector:
    def __init__(self, host, user, pwd, database="geolocation", logger=logging.Logger(__name__)):
        self.logger = logger
        self.logger.info(f"Connecting to the database {database} on the host: {host}.")
        try:
            self.db_conn = mysql.connector.connect(
                host=host,
                user=user,
                password=pwd,
                database=database
                )
            self.cursor = self.db_conn.cursor()
            self.logger.info(f"Connection to database {database} established successfully.")
        except Exception as e:
            self.logger.error(f"Cannot connect to database {database} on {host}. Error: {e}.")
            raise

    def get_all_registered_devices(self):
        stmt = "SELECT * FROM registered_devices"
        self.cursor.execute(stmt)
        return self.cursor.fetchall()
    