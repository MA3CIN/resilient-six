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

    def get_all_registered_devices(self):
        stmt = "SELECT * FROM Registered_Devices"
        self.cursor.execute(stmt)
        return self.cursor.fetchall()
    
    def get_owners_devices(self, owner_id):
        stmt = "SELECT * FROM Registered_Devices WHERE owner=(%s)"
        self.cursor.execute(stmt, (owner_id, ))
        return self.cursor.fetchall()

    def add_device(self, owner, model):
        if isinstance(model, str):
            self.cursor.execute("SELECT id FROM Models WHERE name=%s", model)
            model_id = self.cursor.fetchone()
        else:
            model_id=model
        stmt = "INSERT INTO Registered_Devices (owner, model) VALUES (%s, %s)"
        try:
            self.cursor.execute(stmt, (owner, model_id))
            self.db_conn.commit()
        except Exception as e:
            self.logger.error(f"Cannot register new device. Error: {e}")
            raise

    def get_all_models(self):
        stmt = "SELECT * FROM Models"
        self.cursor.execute(stmt)
        return self.cursor.fetchall()
    
    def add_model(self, category, manufacturer, name, energy_cons):
        self.logger.info(f"Adding new model {name}.")
        stmt = "INSERT INTO Models (category, manufacturer, name, energy_consumption) VALUES (%s, %s, %s, %s)"
        try:
            self.cursor.execute(stmt, (category, manufacturer, name, energy_cons))
            self.db_conn.commit()
        except Exception as e:
            self.logger.error(f"Cannot add new model. Error: {e}")
            raise

    def get_all_categories(self):
        stmt = "SELECT * FROM Devices_Categories"
        self.cursor.execute(stmt)
        return self.cursor.fetchall()
    
    def add_category(self, name):
        self.logger.info(f"Adding new category {name}.")
        stmt = "INSERT INTO Devices_Categories (name) VALUES (%s)"
        try:
            self.cursor.execute(stmt, (name, ))
            self.db_conn.commit()
        except Exception as e:
            self.logger.error(f"Cannot add new category. Error: {e}")
            raise

    def get_model_id(self, model_name):
        self.cursor.execute("SELECT id FROM Models WHERE name=%s", (model_name, ))
        return self.cursor.fetchone()

    def get_devices_per_model(self, model_id):
        stmt = "SELECT * FROM Registered_Devices WHERE model=(%s)"
        self.cursor.execute(stmt, (model_id, ))
        return self.cursor.fetchall()
    
    def get_model_energy(self, model_id):
        self.cursor.execute("SELECT energy_consumption FROM Models WHERE id=%s", (model_id, ))
        return self.cursor.fetchone()

    # def get_device(self, device_id):
    #     self.logger.info(f"Getting information about device {device_id}.")
    #     try:
    #         stmt="SELECT * FROM registered_devices WHERE id=%s"
    #         self.cursor.execute(stmt, (device_id, ))
    #     except Exception as e:
    #         self.logger.error(f"Cannot fetch devices {device_id} information. Error: {e}.")
    #         raise
    #     return self.cursor.fetchone()
    