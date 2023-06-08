from flask import *
import pandas as pd
from sklearn.linear_model import LogisticRegression

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/rain')
def rain_page():
    return render_template("rain.html")

# Home route
@app.route('/live_sensor_data')
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
    app.run(debug=True)
