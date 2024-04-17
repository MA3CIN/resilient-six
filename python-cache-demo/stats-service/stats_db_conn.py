import mysql.connector
import logging

class StatisticsDBConnector:
    def __init__(self, host, user, pwd, database="statistics", logger=logging.Logger(__name__)):
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

    def get_all_metrics(self):
        stmt = "SELECT id, name FROM Metrics"
        self.cursor.execute(stmt)
        return self.cursor.fetchall()
    
    def get_device_all_metrics(self, device_id):
        stmt = "SELECT id, name from Metrics WHERE id IN (SELECT DISTINCT metric_id from Observed_Values WHERE device_id=(%s))"
        self.cursor.execute(stmt, (device_id, ))
        return self.cursor.fetchall()
    
    def get_recent_values(self, device_id, metric_id, max_number):
        stmt = "SELECT value, timestamp from Observed_Values WHERE device_id=(%s) AND metric_id=(%s) ORDER BY timestamp DESC LIMIT %s"
        self.cursor.execute(stmt, (device_id, metric_id, int(max_number)))
        return self.cursor.fetchall()    

    def get_values_per_device_and_metric(self, devices_ids, metric_id):
        stmt = """  SELECT ov.device_id, ov.metric_id, ov.value, ov.timestamp FROM Observed_Values ov 
                    JOIN (
                        SELECT device_id, metric_id, MAX(timestamp) AS max_timestamp
                        FROM Observed_Values
                        WHERE device_id IN (%s)
                        GROUP BY device_id, metric_id
                    ) recent_values
                    ON ov.device_id = recent_values.device_id AND ov.timestamp = recent_values.max_timestamp AND ov.metric_id = recent_values.metric_id
                    WHERE ov.metric_id = %s;"""
        self.cursor.execute(stmt, (devices_ids, metric_id))
        return self.cursor.fetchall()            
