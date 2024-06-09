from models import GeolocationModel
from flask import Flask, request, jsonify
from utils import *

app = Flask(__name__)

db = GeolocationModel()

@app.route('/positions/<id>', methods=['GET'])
def device_position_get(id):
    try:
      pos_x, pos_y = db.device_position_get(id)
    except Exception as e:
       response = {
          "Error": str(e)
        }
       return jsonify(response)
    response = {
      "x_pos": pos_x, 
      "y_pos": pos_y
    }
    return jsonify(response)

@app.route('/positions', methods=['POST'])
def device_position_add():
    data = request.get_json()
    try:
      id = int(data["device_id"])
      pos_x = float(data["x_val"])
      pos_y = float(data["y_val"])
    except Exception as e:
        print("Error at /positions", e)
    try:
       db.device_position_add(id, pos_x, pos_y)
    except Exception as e:
      response = {
          "Error": str(e)
      }
      print("Error at /positions/ll", e)
      return jsonify(response)
    return jsonify(success=True)

if __name__ == '__main__':
    app.run()
