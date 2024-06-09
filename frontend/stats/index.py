from models import StatisticsModel
from flask import Flask, request, jsonify
from utils import *

app = Flask(__name__)

db = StatisticsModel()

@app.route('/metrics', methods=['GET'])
def metrics_get():
    metrics_db = db.metrics_get()
    metrics = jsonify(metrics_to_json(metrics_db))
    return metrics

@app.route('/metrics/device/<id>', methods=['GET'])
def metrics_get_by_device(id):
    metrics_db = db.metrics_get_by_device(id)
    metrics = jsonify(metrics_to_json(metrics_db))
    return metrics

@app.route('/values/devices/<device>/<metric>', methods=['GET'])
def get_recent_values(device, metric):
    rov_db = db.values_get_by_device_metric(device, metric)
    rov = jsonify(recent_values_to_json(rov_db))
    return rov  

if __name__ == '__main__':
    app.run()
