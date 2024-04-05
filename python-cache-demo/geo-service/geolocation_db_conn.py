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

    def get_position(self, device_id):
        stmt = "SELECT pos_x, pos_y FROM positions WHERE id=(%s)"
        self.cursor.execute(stmt, (device_id, ))
        return self.cursor.fetchone()
    
    def add_device_position(self, device_id, pos_x, pos_y):
        if self.check_device_id():
            stmt = "INSERT INTO positions (id, pos_x, pos_y) VALUES (%s, %s, %s)"
            try:
                self.cursor.execute(stmt, (device_id, pos_x, pos_y))
                self.db_conn.commit()
            except Exception as e:
                self.logger.error(f"Cannot add position to device. Error: {e}")
                raise
        else:
            self.logger.error(f"Cannot add position to device {device_id}. Device is not registered or already has assigned position.")

    def check_device_id():
        # TODO: correct function
        return True
    