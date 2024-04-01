from flask import Flask
import random
import os
import mysql.connector

app = Flask(__name__)

DB_URL = os.getenv('DB_URL', 'http://127.0.0.1:3306/') 

mydb = mysql.connector.connect(
  host=DB_URL,
  user="root",
  password="mysql",
  database="devices"
)

@app.route('/', methods=['GET'])
def get_random_number():
    return str(random.randint(1, 100))

@app.route('/db', methods=['GET'])
def get_data_from_db():
    mycursor = mydb.cursor()

    mycursor.execute("SHOW TABLES")

    myresult = mycursor.fetchall()

    return str(myresult)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
