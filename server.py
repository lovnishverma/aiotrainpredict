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

@app.route('/result')
def live_sensor_data():
    return render_template("result.html")

if __name__ == '__main__':
    app.run()
