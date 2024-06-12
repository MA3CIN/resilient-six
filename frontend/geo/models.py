import mysql.connector
from db_config import config

class GeolocationModel:
    def __init__(self):
        try:
            self.db_conn = mysql.connector.connect(**config) # Desemepaquetado de Diccionario
            self.cursor = self.db_conn.cursor()
        except Exception as e:
            print(e)

    def devices_get(self):
        sql = """SELECT device_id from Devices_Locations"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()        

    def device_position_get(self, id):
        sql = """
            SELECT x_position, y_position 
            FROM Devices_Locations 
            WHERE device_id=(%s)
            ORDER BY timestamp DESC
            LIMIT 1;
        """
        self.cursor.execute(sql, (id, ))
        return self.cursor.fetchone()
    
    def device_position_add(self, id, x, y):
        sql = """
            INSERT INTO Devices_Locations (device_id, x_position, y_position) 
            VALUES (%s, %s, %s)
        """
        try:
            self.cursor.execute(sql, (id, x, y))
            self.db_conn.commit()
        except Exception as e:
            print("Error at Models - device_position_add", e)