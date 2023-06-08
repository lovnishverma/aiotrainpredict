from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

# Database connection details
db_host = "localhost"
db_user = "id20783898_sarwan"
db_password = "Sarwan@123"
db_name = "id20783898_sensor"

# Function to establish database connection
def get_db_connection():
    conn = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)
    return conn

# Function to delete a record
def delete_record(tid):
    conn = get_db_connection()
    cursor = conn.cursor()

    delete_sql = "DELETE FROM sensordata WHERE tid = %s"
    cursor.execute(delete_sql, (tid,))
    conn.commit()

    cursor.close()
    conn.close()

# Function to delete all records
def delete_all_records():
    conn = get_db_connection()
    cursor = conn.cursor()

    delete_all_sql = "TRUNCATE TABLE sensordata"
    cursor.execute(delete_all_sql)
    conn.commit()

    cursor.close()
    conn.close()

# Function to retrieve sensor data from the database
def get_sensor_data():
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "SELECT tid, sensorid, samplename, temp, hum, servertimestamp " \
          "FROM sensordata " \
          "ORDER BY tid DESC " \
          "LIMIT 25"

    cursor.execute(sql)
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result

# Home route
@app.route('/')
def index():
    sensor_data = get_sensor_data()
    return render_template('template.html', sensor_data=sensor_data)

# Delete route
@app.route('/delete', methods=['GET'])
def delete():
    tid = request.args.get('tid')
    delete_record(tid)
    return "Data Successfully Deleted"

# Delete all route
@app.route('/delete-all', methods=['POST'])
def delete_all():
    delete_all_records()
    return "All Entries Successfully Deleted"

if __name__ == '__main__':
    app.run()
