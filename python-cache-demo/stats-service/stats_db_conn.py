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
        stmt = "SELECT * FROM Metrics"
        self.cursor.execute(stmt)
        return self.cursor.fetchall()
    
    def get_metric(self, metric_id):
        stmt = "SELECT * from Metrics WHERE id=(%s)"
        self.cursor.execute(stmt, (metric_id, ))
        return self.cursor.fetchone()

    # def get_device_all_metrics(self, device_id):
    #     # TODO: clarify if a metric value is assigned to particular model or maybe single device
    #     stmt = "SELECT metric_id FROM models_metrics WHERE model_id=(%s)"
    #     self.cursor.execute(stmt, (device_id, ))
    #     return self.cursor.fetchall()