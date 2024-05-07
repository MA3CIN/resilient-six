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
DB_URL = os.getenv('DB_URL', 'resilientsix-mysql-db.mysql.database.azure.com')

user="root"
pwd="mysql"

db = GeolocationDBConnector(
  host=DB_URL,
  user=user,
  pwd=pwd,
  database="geolocation"
)

# invalidate cache after 1 hour by default
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
       msg = f"No device with id {device_id} found."
       logger.error(f"{msg}. Error: {e}")
       return jsonify(msg)
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
    api_url = f"{INFRA_URL}devices"
    response = session.get(api_url)
    devices = response.json()
    devices_id_in_db = [int(x[0]) for x in db.get_all_devices_id()]
    # check cache, if all devices ids from the geo db are present in the cache - continue
    # if the cache misses some ids, then invalidate and fetch new data
    if not are_up_to_date_ids(devices.keys(), devices_id_in_db):
      logging.info("Invalidating the cache.")
      session.cache.delete(urls=[api_url])
      response = session.get(api_url)
      logging.info(f"New data fetched from {api_url}.")
      devices = response.json()
    devices_ids_for_owner = [device_id for device_id, device_info in devices.items() if device_info['owner'] == int(owner_id)]
    all_x, all_y = 0, 0
    position_count=0
    for device_id in devices_ids_for_owner:
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

@app.route('/clear-cache', methods=['GET'])
def clear_cache():
    session.cache.clear()
    logging.info("Cache cleared.")
    return jsonify(success=True)

def are_up_to_date_ids(devices_infra, devices_geo):
    if (all (str(x) in devices_infra for x in devices_geo)):
       return True
    else:
       return False

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4001)
