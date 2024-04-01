from infra_db_conn import InfraDBConnector
from flask import Flask, request, jsonify
import logging
import os

app = Flask(__name__)

logger = logging.Logger(__name__)

DB_URL = os.getenv('DB_URL', 'http://127.0.0.1:3306/') 
db = InfraDBConnector(
  host=DB_URL,
  user="test_user",
  pwd="123456",
  database="devices"
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

@app.route('/devices/models', methods=['GET'])
def get_all_models():
    """
    Get all available devices' models.
    """
    logger.info("Getting all available models.")
    return db.get_all_models()

@app.route('/devices/owners/<string:owner_id>', methods=['GET'])
def get_users_devices(owner_id):
    """
    Get all devices belonging to provided user.
    Args:
      owner_id (int): id of the owner.
    """
    logger.info(f"Fetching devices belonging to user with id {owner_id}.")
    return db.get_users_devices(owner_id)

@app.route('/devices', methods=['POST'])
def register_device():
    """
    Registering a device.
    Required input:
      owner (int): id of the owner
      model (int): id of the model
      TODO: maybe we could provide an option to add a name of the model?
      x_pos (float): x position
      y_pos (float): y position
    """
    data = request.get_json()
    try:
      owner = int(data["owner"])
      model = int(data["model"])
      x_pos = float(data["x_pos"])
      y_pos = float(data["y_pos"]) 
    except Exception as e:
        logger.error("Incorrect data provided for registering a device. Error: {e}.")
        raise
    try:
      db.add_device(owner, model, x_pos, y_pos)
      logger.info(f"Devide registered successfully.")
    except Exception as e:
      logger.error(f"Error when registering device. Error: {e}.")
      raise
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
