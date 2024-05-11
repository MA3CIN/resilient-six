
from infra_db_conn import InfraDBConnector
from flask import Flask, request, jsonify
import logging
import os

app = Flask(__name__)

logger = logging.Logger(__name__)

DB_URL = os.getenv('DB_URL', 'http://127.0.0.1:3306/') 

db = InfraDBConnector(
  host=DB_URL,
  user = "admin_user",
  pwd = "admin_password",
  database="devices"
)

@app.route('/devices', methods=['GET'])
def get_all_registered_devices():
    """
    Get all registered devices.
    """
    logger.info("Getting all registered devices.")
    devices = db.get_all_registered_devices()
    json_devices = devices_to_json(devices)
    return jsonify(json_devices)

@app.route('/devices/owners/<owner_id>', methods=['GET'])
def get_owners_devices(owner_id):
    """
    Get all registered devices belonging to particular user.
    Required input:
      owner_id (int): id of the owner
    """
    logger.info(f"Getting devices registered for {owner_id}.")
    devices = db.get_owners_devices(owner_id)
    json_devices = devices_to_json(devices)
    return jsonify(json_devices)

@app.route('/devices', methods=['POST'])
def register_device():
    """
    Register new device.
    Required input:
      owner (int): id of the owner
      model (int/str): id or name of the model
      TODO: add option to add a name
    """
    data = request.get_json()
    try:
      owner = int(data["owner"])
      model = int(data["model"])
    except Exception as e:
        logger.error("Incorrect data provided for registering a device. Error: {e}.")
        raise
    try:
      db.add_device(owner, model)
      logger.info(f"Devide registered successfully.")
    except Exception as e:
      logger.error(f"Error when registering device. Error: {e}.")
      raise
    return jsonify(success=True)

@app.route('/models', methods=['GET'])
def get_all_models():
    """
    Get all available devices' models.
    """
    logger.info("Getting all available models.")
    return db.get_all_models()

@app.route('/models', methods=['POST'])
def add_model():
    """
    Add new model.
    Required input:
      category (int): id of the category
      manufacturer (int): id of the manufacturer
      name (str): name of the model
      energy_cons (float): energy consumption of the model
    """
    logger.info("Adding new model.")
    data = request.get_json()
    try:
      category = int(data["category"])
      name = str(data["name"])
      manufacturer = int(data["manufacturer"])
      energy_cons = float(data["energy_cons"])
    except Exception as e:
        logger.error("Incorrect data provided for adding a model. Error: {e}.")
        raise
    try:
      db.add_model(category, manufacturer, name, energy_cons)
      logger.info(f"Model {name} added successfully.")
    except Exception as e:
      logger.error(f"Error when adding model. Error: {e}.")
      raise
    return jsonify(success=True)

@app.route('/categories', methods=['GET'])
def get_all_categories():
    """
    Get all available models' categories.
    """
    logger.info("Getting all available categories.")
    return db.get_all_categories()

@app.route('/categories', methods=['POST'])
def add_category():
    """
    Add new category.
    Required input:
      name (str): name of the category
    """
    logger.info("Adding new category.")
    data = request.get_json()
    try:
      name = str(data["name"])
    except Exception as e:
        logger.error("Incorrect data provided for adding a category. Error: {e}.")
        raise
    try:
      db.add_category(name)
      logger.info(f"Category {name} added successfully.")
    except Exception as e:
      logger.error(f"Error when adding category. Error: {e}.")
      raise
    return jsonify(success=True)

@app.route('/getConsumption/models/<model_name>', methods=['GET'])
def get_model_consumption(model_name: str):
    """
    Get calculated energy consumption for all devices from provided model.
    """
    logger.info(f"Getting total energy consumption for devices of model {model_name}.")
    try:
      model_id = db.get_model_id(model_name)[0]
      devices = db.get_devices_per_model(model_id)
      energy_cons = db.get_model_energy(model_id)[0]
    except Exception as e:
      logger.error(f"Problem with fetching data for {model_name} devices consumption. Error {e}")
      raise
    total_energy_cons = energy_cons * len(devices)
    logger.info(f"Total energy consumption for devices from model {model_name} equals {total_energy_cons}.")
    return jsonify({"model_id":model_id,"model_name":model_name,"total_energy_consumption": total_energy_cons})

def devices_to_json(devices):
   devices_json = {}
   for device in devices:
      id = device[0]
      devices_json[id] = {"id": id, "model": device[1], "owner": device[2], "name": device[3], "comment": device[4]}
   return devices_json

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
