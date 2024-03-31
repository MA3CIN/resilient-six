import mysql.connector
import logging

class InfraDBConnector:
    def __init__(self, host, user, pwd, database="devices", logger=logging.Logger(__name__)):
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

    def add_device(self, owner, model, x_pos, y_pos):
        if isinstance(model, str):
            self.cursor.execute("SELECT id FROM models WHERE name=%s", model)
            model_id = self.cursor.fetchone()
        else:
            model_id=model
        stmt = "INSERT INTO registered_devices (owner, model, x_position, y_position) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(stmt, (owner, model_id, x_pos, y_pos))
        self.db_conn.commit()

    def get_device(self, device_id):
        self.logger.info(f"Getting information about device {device_id}.")
        try:
            stmt="SELECT * FROM registered_devices WHERE id=%s"
            self.cursor.execute(stmt, (device_id, ))
        except Exception as e:
            self.logger.error(f"Cannot fetch devices {device_id} information. Error: {e}.")
            raise
        return self.cursor.fetchone()

    def get_users_devices(self, owner):
        stmt = "SELECT * FROM registered_devices WHERE owner=%s"
        self.cursor.execute(stmt, (owner, ))
        return self.cursor.fetchall()

    def get_all_registered_devices(self):
        stmt = "SELECT * FROM registered_devices"
        self.cursor.execute(stmt)
        return self.cursor.fetchall()
    
    def get_all_models(self):
        stmt = "SELECT * FROM models"
        self.cursor.execute(stmt)
        return self.cursor.fetchall()
    