import requests
import json

def categories_get():
    url_categories = "http://127.0.0.1:3000/categories"
    response = requests.get(url_categories).json()
    options = [(value['id'], value['name'].title()) for key, value in response.items()] # convertimos en lista(mas facil de manipular)
    return options

def models_get_by_category(category):
    url_models = "http://127.0.0.1:3000/models"
    response = requests.get(url_models).json()
    options = [(value['id'], value['name'].title()) for key, value in response.items() if value['category'] == category]
    return options

def manufacturers_get():
    url_models = "http://127.0.0.1:3000/manufacturers"
    response = requests.get(url_models).json()
    options = [(value['id'], value['name'].title()) for key, value in response.items()]
    return options

def model_add_to_service(data):
    success  = True
    try:
        url = 'http://127.0.0.1:3000/models'
        headers = {'Content-Type': 'application/json'}
        data_json = json.dumps(data)
        respuesta = requests.post(url, data = data_json, headers = headers)
        respuesta.raise_for_status()
    except requests.exceptions.RequestException as e:
        success = False
        print(f'Error en la solicitud POST: {e}')
    return success

def devices_all():
    url_devices = "http://127.0.0.1:3000/models/full"
    response = requests.get(url_devices).json()
    devices = [[value['model_id'], value['model_name'].title(), value['category_name'].title(), value['manufacturer_name'].title()] 
               for key, value 
               in response.items()]
    return devices

def devices_all_w_geo():
    #Get all devices
    url_devices = "http://127.0.0.1:3000/models/full"
    devices_response = requests.get(url_devices).json()
    devices = [[value['model_id'], value['model_name'].title(), value['category_name'].title(), value['manufacturer_name'].title()] 
               for key, value 
               in devices_response.items()]
    # retrieve geo information (from the ones that have it)
    geo_data = geo_get(len(devices))
    # update (mix) two dicts
    response = update_data_with_coordinates(devices, geo_data)
    return response

def geo_get(ids):
    response = []
    for id in range(ids+1):
        url_geo = f"http://127.0.0.1:3001/positions/{id}"
        geo_response = requests.get(url_geo).json()
        if 'Error' not in geo_response:
            response.append([id, geo_response['x_pos'], geo_response['y_pos']])        
    return response

def geo_add(data):
    success  = True
    try:
        url = 'http://127.0.0.1:3001/positions'
        headers = {'Content-Type': 'application/json'}
        data_json = json.dumps(data)
        respuesta = requests.post(url, data = data_json, headers = headers)
        respuesta.raise_for_status()
    except requests.exceptions.RequestException as e:
        success = False
        print(f'Error en la solicitud POST: {e}')
    return success

def update_data_with_coordinates(devices, geo):
    geo2 = {item[0]: item[1:] for item in geo}

    # Actualizar data1 con los valores de x_pos y y_pos de dict_data2
    data_updated = []
    for item in devices:
        model_id = item[0]
        if model_id in geo2:
            x_pos, y_pos = geo2[model_id]
            data_updated.append(item + [x_pos, y_pos])
        else:
            data_updated.append(item)
    return data_updated    

def device_get(id):
    url_categories = f"http://127.0.0.1:3000/model/{id}"
    device = requests.get(url_categories).json()
    return device

def get_metrics_by_device_id(id):
    url_metrics = f"http://127.0.0.1:3002/metrics/device/{id}"
    response = requests.get(url_metrics).json()
    metrics = [(value['id'], value['name']) for key, value in response.items()]
    return metrics

def metrics_values_by_device(id_device, id_metric):
    url_metrics = f"http://127.0.0.1:3002/values/devices/{id_device}/{id_metric}"
    response = requests.get(url_metrics).json()
    return response