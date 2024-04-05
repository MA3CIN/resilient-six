from geolocation_db_conn import GeolocationDBConnector
from flask import Flask, request, jsonify
import logging
import os
from requests_cache import CachedSession
import requests
import requests_cache

app = Flask(__name__)

logger = logging.Logger(__name__)

# invalidate cache after 1 hour
session = CachedSession('infra_owners_cache', backend='sqlite', expire_after=3600)

INFRA_URL = os.getenv('INFRA_URI', 'http://127.0.0.1:3000/') 
DB_URL = os.getenv('DB_URL', 'http://127.0.0.1:3000/') 

db = GeolocationDBConnector(
  host=DB_URL,
  user="root",
  pwd="mysql",
  database="geolocation"
)


@app.route('/positions/<int:device_id>', methods=['GET'])
def get_device_position(device_id):
    """
    Get position of given device.
    """
    logger.info(f"Getting positions about device {device_id}.")
    pos_x, pos_y = db.get_position(device_id)
    response_dict = {"pos_x": pos_x, "pos_y": pos_y}
    logger.info(f"Device's {device_id} position: x={pos_x}, y={pos_y}")
    return response_dict

@app.route('/positions', methods=['POST'])
def add_new_device_position():
    """
    Add new device's position.
    Required input:
      device_id (int): id of the device
      pos_x (float): position x of the device
      pos_y (float): position y of the device
    """
    data = request.get_json()
    try:
      device_id = int(data["device_id"])
      pos_x = float(data["pos_x"])
      pos_y = float(data["pos_y"])
    except Exception as e:
        logger.error("Incorrect data provided for adding position to device. Error: {e}.")
        raise
    try:
      db.add_device_position(device_id, pos_x, pos_y)
      logger.info(f"Position to device with id {device_id} added successfully.")
    except Exception as e:
      logger.error(f"Error when adding new position to device. Error: {e}.")
      raise
    return jsonify(success=True)

# @app.route('/', methods=['GET'])
# def get_location_for_gate():
#     returner_owners = get_owners()
#     return(str(returner_owners.json()))

# # get endpoint IF cache is empty. 
# #invalidate cache if you have a serial number without a corresponding cached owner 
# #with cache enabled
# def get_owners():
#    if (INFRA_URL in session.cache.urls()):
#       print("gotten from cache")
#    else:
#       print("gotten manually")
#    return session.get(INFRA_URL)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
