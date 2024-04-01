from geolocation_db_conn import GeolocationDBConnector
from flask import Flask
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
