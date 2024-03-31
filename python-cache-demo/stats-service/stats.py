from flask import Flask
import random
import os

infra_svc_endpoint_address = os.getenv('INFRA_URI', 'http://127.0.0.1:3000/')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_random_number():
    return str(random.randint(1, 100))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
