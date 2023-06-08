from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression

app = Flask(__name__)

@app.route('/')
def indexpage():
    return render_template("index.html")

@app.route('/live_sensor_data')
def live_sensor_data_page():
    return render_template("live_sensor_data.html")

@app.route('/rain')
def rainpage():
    return render_template("rain.html")

@app.route("/rain-predict", methods=["POST"])
def rainpredict():
    sw = float(request.form.get("sw"))
    sh = float(request.form.get("sh"))
    pw = float(request.form.get("pw"))
    
    url = "https://raw.githubusercontent.com/priyanka9-99/aiot/main/test.csv"
    dfspf = pd.read_csv(url)
    X = dfspf.iloc[:, 0:3]  # Select all rows and first three columns as input X
    Y = dfspf.iloc[:, 3]    # Select all rows and the fourth column as output Y
    
    model2 = LogisticRegression()
    model2.fit(X, Y)
    
    arr = model2.predict([[sw, sh, pw]])
    
    return render_template("rain.html", data=str(arr[0]) + " mm")

@app.route('/result')
def resultpage():
    return render_template("result.html")

@app.route("/live-sensor-data-predict", methods=["POST"])
def live_sensor_data_predict():
    # Retrieve the data from the live sensor form
    # Perform the necessary calculations or predictions
    # Return the result to the live_sensor_data.html template
    return render_template("live_sensor_data.html")

if __name__ == '__main__':
    app.run()
