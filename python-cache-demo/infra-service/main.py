from flask import Flask
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_random_number():
    return str(random.randint(1, 100))

if __name__ == '__main__':
    app.run(port=5000)
