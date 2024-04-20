from geolocation_db_conn import GeolocationDBConnector
from flask import Flask, request, jsonify
import logging
import os
from requests_cache import CachedSession

app = Flask(__name__)

logger = logging.Logger(__name__)
logging.basicConfig(level=logging.DEBUG)

DECIMALS = 3
INFRA_URL = os.getenv('INFRA_URL', 'http://127.0.0.1:3000') 
DB_URL = os.getenv('DB_URL', 'http://127.0.0.1:3306') 

user="root"
pwd="mysql"

db = GeolocationDBConnector(
  host=DB_URL,
  user=user,
  pwd=pwd,
  database="geolocation"
)

# invalidate cache after 1 hour
#TODO: should we add a check and invalidate cache once some data changes for the owners?
session = CachedSession('geo_infra_owners_cache', backend='sqlite', expire_after=3600)

@app.route('/positions/<device_id>', methods=['GET'])
def get_device_position(device_id):
    """
    Get position of given device.
    Required input:
      device_id (int): id of the device
    """
    logger.info(f"Getting positions about device {device_id}.")
    try:
      pos_x, pos_y = db.get_position(device_id)
    except Exception as e:
       logger.error(f"No device with id {device_id} found. Error: {e}")
       return None
    response_dict = {"position_x": pos_x, "position_y": pos_y}
    logger.info(f"Device's {device_id} position: x={pos_x}, y={pos_y}")
    return jsonify(response_dict)

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

@app.route('/positions/recommend/<owner_id>', methods=['GET'])
def get_recommended_position(owner_id):
    """
    Get recommended position for owner's device.
    Calculated as:
    - pos_x: average of x_positions from all user's devices
    - pos_y: average of y_positions from all user's devices
    Simulates some more complex computations.

    Required input:
      owner_id (int): id of the owner
    """
    logger.info(f"Getting devices for {owner_id}.")
    api_url = f"{INFRA_URL}/devices/owners/{owner_id}"
    response = session.get(api_url)
    devices = response.json()
    all_x, all_y = 0, 0
    position_count=0
    for device_id in devices.keys():
      try:
        pos_x, pos_y = db.get_position(int(device_id))
        all_x += pos_x
        all_y+=pos_y
        position_count+=1
      except Exception as e:
         logger.error(f"Device with id: {device_id} does not have position yet.")
    if position_count:
      pos_x = round(all_x/position_count, DECIMALS)
      pos_y=round(all_y/position_count, DECIMALS)
    else:
       # default values: (0, 0)
       pos_x, pos_y = 0, 0
    logger.info(f"Recommendation created: (pos_x={pos_x}, pos_y={pos_y})")
    return jsonify({"position_x": pos_x, "position_y": pos_y})

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
    app.run(host='0.0.0.0', port=4001)
