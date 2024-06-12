import mysql.connector
from db_config import config

class StatisticsModel:
    def __init__(self):
        try:
            self.db_conn = mysql.connector.connect(**config) #Desemepaquetado de Diccionario
            self.cursor = self.db_conn.cursor()
        except Exception as e:
            print("Error in connection:" ,e)

    def metrics_get(self):
        sql = """
            SELECT id, name 
            FROM Metrics
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def metrics_get_by_device(self, id):
        sql = """
            SELECT id, name from Metrics 
            WHERE id 
            IN (SELECT DISTINCT metric_id 
                FROM Observed_Values 
                WHERE 
                device_id=%s
            )
        """
        self.cursor.execute(sql, (id, ))
        return self.cursor.fetchall()
    
    # def values_get_recent(self, device, metric, max):
    #     sql = """
    #         SELECT value, timestamp from Observed_Values 
    #         WHERE device_id=%s AND metric_id=%s 
    #         ORDER BY timestamp 
    #         DESC LIMIT %s
    #         """
    #     self.cursor.execute(sql, (device, metric, int(max)))
    #     return self.cursor.fetchall() 

    def values_get_by_device_metric(self, device, metric):
        sql = """  
            SELECT value 
            FROM Observed_Values 
            WHERE device_id LIKE (%s) 
            AND metric_id like (%s)
            """
        self.cursor.execute(sql, (device, metric))
        return self.cursor.fetchall() 



