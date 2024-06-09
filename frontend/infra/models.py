import mysql.connector
from db_config import config

class DeviceModel:
    def __init__(self):
        try:
            self.db_conn = mysql.connector.connect(**config) #Desemepaquetado de Diccionario
            self.cursor = self.db_conn.cursor()
        except Exception as e:
            print(e)

    def get_all_registered_devices(self):
        sql = """
                SELECT id, model, owner, name, comments 
                FROM Registered_Devices
            """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_owners_devices(self, id):
        sql = """
            SELECT id, model, owner, name, comments 
            FROM Registered_Devices WHERE owner=%s
            """
        self.cursor.execute(sql, (id,))
        return self.cursor.fetchall()

    def add_device(self, owner, model):
        if isinstance(model, str):
            self.cursor.execute("SELECT id FROM Models WHERE name=%s", (model,))
            model_id = self.cursor.fetchone()[0]
        else:
            model_id = model

        sql = "INSERT INTO Registered_Devices (owner, model) VALUES (%s, %s)"
        try:
            self.cursor.execute(sql, (owner, model_id))
            self.db_conn.commit()
        except Exception as e:
            raise

    def models_all(self):
        sql = """SELECT * FROM Models"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def models_all_category_manufacturers(self):
        sql = """
            SELECT
                Models.id AS model_id,
                Models.name AS model_name,
                (SELECT name FROM Devices_Categories WHERE id = Models.category) AS category_name,
                (SELECT name FROM Manufacturers WHERE id = Models.manufacturer) AS manufacturer_name,
                Models.energy_consumption,
                Models.comments
            FROM
                Models
            ORDER BY
                model_id;
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def model_category_manufacturer(self, id):
        sql = """
            SELECT
                Models.id AS model_id,
                Models.name AS model_name,
                (SELECT name FROM Devices_Categories WHERE id = Models.category) AS category_name,
                (SELECT name FROM Manufacturers WHERE id = Models.manufacturer) AS manufacturer_name
            FROM
                Models
            WHERE
                id=%s
        """
        self.cursor.execute(sql, (id,))
        return self.cursor.fetchone()
    
    def manufacturers_all(self):
        sql = """SELECT * FROM Manufacturers"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def model_add(self, manufacturer, category, name, energy_cons):
        sql = """
            INSERT INTO Models (category, manufacturer, name, energy_consumption) 
            VALUES (%s, %s, %s, %s)"""
        try:
            self.cursor.execute(sql, (category, manufacturer, name, energy_cons))
            self.db_conn.commit()
        except Exception as e:
            print(f"Error at model_add: {e}")

    def categories_all(self):
        sql = """SELECT * FROM Devices_Categories"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def add_category(self, name):
        stmt = "INSERT INTO Devices_Categories (name) VALUES (%s)"
        try:
            self.cursor.execute(stmt, (name,))
            self.db_conn.commit()
        except Exception as e:
            raise

    def model_by_id(self, name):
        self.cursor.execute("SELECT id FROM Models WHERE name=%s", (name,))
        return self.cursor.fetchone()[0]

    def devices_by_model(self, id):
        sql = """SELECT * FROM Registered_Devices WHERE model=%s"""
        self.cursor.execute(sql, (id,))
        return self.cursor.fetchall()

    def model_energy(self, id):
        self.cursor.execute("SELECT energy_consumption FROM Models WHERE id=%s", (id,))
        return self.cursor.fetchone()[0]