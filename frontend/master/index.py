from flask import Flask, render_template, request, flash, jsonify, redirect, url_for
from models import *
from utils import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'REsiLient-6iX'

@app.route("/", methods=['GET'])
def home():
    return render_template('home.html')

@app.route("/device/add", methods=['GET'])
def device_add():
    categories_db = categories_get()
    manufacturers_db = manufacturers_get()
    return render_template('device_add.html', 
                    categories = categories_db,
                    manufacturers = manufacturers_db)

@app.route('/models/<int:category>', methods=['GET'])
def models_add(category):
    models = models_get_by_category(category)
    return models

@app.route('/models/add', methods=['POST'])
def models_add_post():
    if validar_campos(request.form):
        # Conver Data to JSON bcause infra recieves in JSON format
        form_data = request.form.to_dict()
        # post request 
        model_add_to_service(form_data)
        flash('Device Added successfully!', 'success')
    else:
        flash('Somethign goes wrong, try again!', 'error')
    return render_template('home.html')

@app.route("/devices", methods=['GET'])
def device_list():
    devices_db = devices_all()
    return render_template('device_list.html', devices = devices_db)

@app.route("/geo", methods=['GET'])
def geo_list():
    devices_db = devices_all_w_geo()
    return render_template('geo_list.html', devices = devices_db)

@app.route("/geo/add/<int:id>", methods=['GET'])
def geo_device_get(id):
    device = device_get(id)
    return render_template('geo_detail.html', device = device)

@app.route("/geo/add/", methods=['POST'])
def geo_add_position():
    if validar_campos(request.form):
        # Conver Data to JSON bcause infra recieves in JSON format
        form_data = request.form.to_dict()
        # post request 
        geo_add(form_data)
        flash('Geolocation Data Added successfully!', 'success')
    else:
        flash('Somethign goes wrong with the data, try again!', 'error')
    return render_template('home.html')

@app.route("/stats", methods=['GET'])
def stats_add():
    devices_db = devices_all()
    return render_template('stats_find.html', devices = devices_db)

@app.route("/metrics/device/<int:id>", methods=['GET'])
def metrics_by_device_id(id):
    metrics_db = get_metrics_by_device_id(id)
    metrics = jsonify(metrics_to_json(metrics_db))
    return metrics

@app.route("/metrics", methods=['POST'])
def metrics_post():
    if validar_campos(request.form):
        form_data = request.form
        device_id = form_data.get('device')
        device_name = form_data.get('device_text')
        metric_id = form_data.get('metrics')
        metric_name = form_data.get('metrics_text')
        data = metrics_values_by_device(device_id, metric_id)
        if len(data) >= 2: #bcause it needs at least 2 values to build the statistics 
            return render_template('stats_result.html', 
                device_name = device_name,
                metric_name = metric_name,
                mean = getMean(data),
                std_dev = getSDev(data),
                avg = getAVG(data)
            )
        else:
            flash("Selected device doesn't have enough observations to build statistics", 'error')
            return redirect(url_for('stats_add'))
    else:
        flash('Somethign goes wrong with the data, try again!', 'error')
        return render_template('home.html')

@app.route("/logout", methods=['GET'])
def app_logout():
    return render_template('login.html')

if __name__ == "__main__":
    app.run()
