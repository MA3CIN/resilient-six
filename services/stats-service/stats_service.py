from stats_db_conn import StatisticsDBConnector
from flask import Flask, jsonify
import logging
import os
from requests_cache import CachedSession

app = Flask(__name__)

logger = logging.Logger(__name__)

infra_svc_endpoint_address = os.getenv('INFRA_URL', 'http://127.0.0.1:3000/')
INFRA_URL = os.getenv('INFRA_URL', 'http://127.0.0.1:3000') 
DB_URL = os.getenv('DB_URL', 'http://127.0.0.1:3306/') 

db = StatisticsDBConnector(
  host=DB_URL,
  user="root",
  pwd="mysql",
  database="statistics"
)

# invalidate cache after 1 hour
session = CachedSession('stats_infra_owners_cache', backend='sqlite', expire_after=3600)

@app.route('/metrics', methods=['GET'])
def get_all_metrics():
    """
    Get all available metrics.
    """
    logger.info("Getting all available metrics.")
    result = db.get_all_metrics()
    metrics = metrics_to_json(result)
    return jsonify(metrics)

@app.route('/metrics/devices/<device_id>', methods=['GET'])
def get_device_all_metrics(device_id):
    """
    Get all available metrics for chosen device.
    Required input:
      device_id (int): id of the device
    """
    logger.info(f"Getting all distinct available metrics for device {device_id}.")
    result = db.get_device_all_metrics(device_id)
    metrics = metrics_to_json(result)
    return jsonify(metrics)

@app.route('/values/devices/<device_id>/<metric_id>/<max_number>', methods=['GET'])
def get_recent_values(device_id, metric_id, max_number):
    """
    Get max_number of most recent observed values for chosen metric and device.
    Required input:
      device_id (int): id of the device
      metric_id (int): id of the metric
      max_number (int): max number of inquired observed values
    """
    logger.info(f"Getting {max_number} of most recent observed values for device {device_id}.")
    result = db.get_recent_values(device_id, metric_id, max_number)
    obs_values = values_to_json(result)
    return jsonify(obs_values)

@app.route('/values/owner/<owner_id>/metrics/<metric_id>', methods=['GET'])
def get_values_for_owner_by_metric(owner_id, metric_id):
    """
    Get latest observed value for specified metric from all owner's devices.
    Returns list of latest observed values of particular metric,
    for all devices with that metric belonging to provided user id.
    Required input:
      owner_id (int): id of the owner
      metric_id (int): id of the metric
    """
    logger.info(f"Getting latest value for metric {metric_id} of all devices owner's {owner_id}.")
    api_url = f"{INFRA_URL}/devices/owners/{owner_id}"
    response = session.get(api_url)
    devices = response.json()
    devices_ids = devices.keys()
    devices_str_list = ','.join(devices_ids)
    result = db.get_values_per_device_and_metric(devices_str_list, metric_id)
    dict_result = full_observed_values_to_json(result)
    return jsonify(dict_result)  

@app.route('/stats/devices/<device_id>/<metric_id>/<count>', methods=['GET'])
def get_stats_for_device_metric_by_count(device_id, metric_id, count):
    """
    Get statistics about most recent <count> number of device_id for metric_id.
    Returns statistics calculated from get_stats function.
    Required input:
      device_id (int): id of the device
      metric_id (int): id of the metric
      count (int): number of required latest observed values
    """
    logger.info(f"Getting {count} of most recent observed values for device {device_id}.")
    result = db.get_recent_values(device_id, metric_id, count)
    values_list = [float(x[0]) for x in result]
    stats = create_stats(values_list)
    return jsonify(stats)   

@app.route('/clear-cache', methods=['GET'])
def clear_cache():
    session.cache.clear()
    logger.info("Cache cleared.")
    return jsonify(success=True)

def metrics_to_json(metrics):
   metrics_json = {}
   for metric in metrics:
      id = metric[0]
      metrics_json[id] = {"id": id, "name": metric[1]}
   return metrics_json

def values_to_json(values):
    values_list = []
    for value in values:
      values_list.append({"value": value[0], "timestamp": str(value[1])})
    return values_list

def full_observed_values_to_json(values):
    values_list = []
    for value in values:
      values_list.append({"id": value[0], "metric": value[1], "value": value[2], "timestamp": str(value[3])})
    return values_list

def create_stats(values):
    """
    Calculates statistics:
    - min
    - max
    - average
    """
    stats = {"min": min(values), "max": max(values), "avg": round(sum(values)/len(values), 2)}
    return stats

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
