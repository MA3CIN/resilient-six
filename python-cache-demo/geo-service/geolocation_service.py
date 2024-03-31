from geolocation_db_conn import GeolocationDBConnector
from flask import Flask
import logging

app = Flask(__name__)

logger = logging.Logger(__name__)

db = GeolocationDBConnector("localhost", "test_user", "123456", "geolocation")

@app.route('/devices', methods=['GET'])
def get_all_registered_devices():
    """
    Get all registered devices.
    """
    logger.info("Getting all registered devices.")
    return db.get_all_registered_devices()

@app.route('/devices/position/<int:device_id>', methods=['GET'])
def get_device_position(device_id):
    """
    Get all registered devices.
    """
    logger.info(f"Getting information about device {device_id}.")
    device = db.get_device(device_id)
    response_dict = {"pos_x": device[3], "pos_y": device[4]}
    return response_dict

if __name__ == '__main__':
    app.run(port=5000)
