from stats_db_conn import StatisticsDBConnector
from flask import Flask
import logging
import os
import random

app = Flask(__name__)

logger = logging.Logger(__name__)

infra_svc_endpoint_address = os.getenv('INFRA_URI', 'http://127.0.0.1:3000/')
DB_URL = "localhost"

db = StatisticsDBConnector(
  host=DB_URL,
  user="root",
  pwd="mysql",
  database="statistics"
)

# @app.route('/', methods=['GET'])
# def get_random_number():
#     return str(random.randint(1, 100))

@app.route('/metrics', methods=['GET'])
def get_all_metrics():
    """
    Get all available metrics.
    """
    logger.info("Getting all available metrics.")
    return db.get_all_metrics()

# @app.route('/metrics/devices/<int:device_id>', methods=['GET'])
# def get_all_device_metrics(device_id):
#     # TODO: clarify if a metric value is assigned to particular model or maybe single device
#     """
#     Get all metrics for chosen device.
#     Required input:
#       device_id (int): id of the device
#     """
#     logger.info(f"Getting all available metrics for device {device_id}.")
#     metrics_ids = db.get_device_all_metrics(device_id)
#     metrics = [db.get_metric(metric_id) for metric_id in metrics_ids]

#     return db.get_all_device_metrics(device_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
