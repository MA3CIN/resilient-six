from stats_db_conn import StatisticsDBConnector
from flask import Flask
import logging
import os
import random

app = Flask(__name__)

logger = logging.Logger(__name__)

infra_svc_endpoint_address = os.getenv('INFRA_URI', 'http://127.0.0.1:3000/')

# db = StatisticsDBConnector(
#   host="localhost",
#   user="root",
#   pwd="mysql",
#   database="statistics"
# )

@app.route('/', methods=['GET'])
def get_random_number():
    return str(random.randint(1, 100))

# @app.route('/metrics', methods=['GET'])
# def get_all_metrics():
#     """
#     Get all available metrics.
#     """
#     logger.info("Getting all available metrics.")
#     return db.get_all_metrics()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
