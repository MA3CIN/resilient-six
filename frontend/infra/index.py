
from models import DeviceModel
from flask import Flask, request, jsonify
from utils import *

app = Flask(__name__)

db = DeviceModel()

@app.route('/devices', methods=['GET'])
def devices():
    devices_db = db.get_all_registered_devices()
    devices = jsonify(devices_to_json(devices_db))
    return devices

@app.route('/devices/owner/<id>', methods=['GET'])
def devices_by_owner(id):
    devices_db = db.get_owners_devices(id)
    devices = jsonify(devices_to_json(devices_db))
    return devices

@app.route('/devices', methods=['POST'])
def device_add():
    data = request.get_json()
    try:
      owner = int(data["owner"])
      model = int(data["model"])
    except Exception as e:
        print("Error at /devices", e)
    try:
      db.add_device(owner, model)
    except Exception as e:
      print("Error at /devices", e)
    return jsonify(success=True)

@app.route('/models', methods=['GET'])
def models():
    models_db = db.models_all()
    models = jsonify(models_to_json(models_db))
    return models

@app.route('/models', methods=['POST'])
def models_add():
    data = request.get_json()
    try:
      category = int(data["category"])
      name = str(data["name"])
      manufacturer = int(data["manufacturer"])
      energy_cons = float(data["energy_cons"])
    except Exception as e:
        print("Error in /models", e)
        raise
    try:
      db.model_add(manufacturer, category, name, energy_cons)
      print(f"Model {name} added successfully.")
    except Exception as e:
      print(f"Error at /models: {e}.")
    return jsonify(success = True)

@app.route('/model/<int:id>', methods=['GET'])
def model_add(id):
    device_db = db.model_category_manufacturer(id)
    device = {
        "model_id": device_db[0],
        "model_name": device_db[1],
        "category_name": device_db[2],
        "manufacturer_name": device_db[3],
    }
    return jsonify(device)

@app.route('/models/full', methods=['GET'])
def models_all():
   models_db = db.models_all_category_manufacturers()
   models = jsonify(devices_to_json_full(models_db))
   return models 

@app.route('/getConsumption/models/<model>', methods=['GET'])
def model_get_consumption(model: str):
    try:
      model_id = db.model_by_id(model)
      devices = db.devices_by_model(model_id)
      energy_cons = db.model_energy(model_id)
    except Exception as e:
      print(f"Error at /getConsumption/models/<model_name>: ", e)
    total_energy_cons = energy_cons * len(devices)
    return jsonify(
       {"model_id":model_id,
        "model_name":model,
        "total_energy_consumption": total_energy_cons
        }
    )

@app.route('/categories', methods=['GET'])
def categories():
    categories_db = db.categories_all()
    categories = jsonify(categories_to_json(categories_db))
    return categories

@app.route('/manufacturers', methods=['GET'])
def manufacturers():
    manufacturers_db = db.manufacturers_all()
    manufacturers = jsonify(categories_to_json(manufacturers_db))
    return manufacturers

@app.route('/categories', methods=['POST'])
def category_add():
    data = request.get_json()
    try:
      name = str(data["name"])
    except Exception as e:
        print("Error at /categories", e)
    try:
      db.add_category(name)
    except Exception as e:
      print("Error at /categories", e)
    return jsonify(success=True)

if __name__ == '__main__':
    app.run()