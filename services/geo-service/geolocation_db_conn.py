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

    def get_all_devices_id(self):
        stmt = "SELECT device_id from Devices_Locations"
        self.cursor.execute(stmt)
        return self.cursor.fetchall()        

    def get_position(self, device_id):
        stmt = "SELECT x_position, y_position FROM Devices_Locations WHERE device_id=(%s)"
        self.cursor.execute(stmt, (device_id, ))
        return self.cursor.fetchone()
    
    def add_device_position(self, device_id, pos_x, pos_y):
        if self.check_device_id():
            stmt = "INSERT INTO Devices_Locations (device_id, x_position, y_position) VALUES (%s, %s, %s)"
            try:
                self.cursor.execute(stmt, (device_id, pos_x, pos_y))
                self.db_conn.commit()
            except Exception as e:
                self.logger.error(f"Cannot add position to device. Error: {e}")
                raise
        else:
            self.logger.error(f"Cannot add position to device {device_id}. Device is not registered or already has assigned position.")

    def check_device_id(self):
        # TODO: correct function
        return True
    