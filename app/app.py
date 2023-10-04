from flask import Flask, jsonify
import mysql.connector

app = Flask(__framefit__)

# Konfigurasi database
db = mysql.connector.connect(
    host="mariadb",
    user="root",
    password="password",
    database="mydatabase"
)

@app.route('/')
def hello_world():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM mytable")
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
