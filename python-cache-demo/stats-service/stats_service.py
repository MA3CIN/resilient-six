from stats_db_conn import StatisticsDBConnector
from flask import Flask
import logging

app = Flask(__name__)

logger = logging.Logger(__name__)

db = StatisticsDBConnector("localhost", "test_user", "123456", "statistics")

@app.route('/metrics', methods=['GET'])
def get_all_metrics():
    """
    Get all available metrics.
    """
    logger.info("Getting all available metrics.")
    return db.get_all_metrics()


if __name__ == '__main__':
    app.run(port=5000)
