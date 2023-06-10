from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/rainpredict')
def rainpredict_form():
    return render_template("rain.html")

@app.route("/rainpredict", methods=["POST"])
def rainpredict():
    sw = eval(request.form.get("sw"))
    sh = eval(request.form.get("sh"))
    pw = eval(request.form.get("pw"))
    url = "https://raw.githubusercontent.com/priyanka9-99/aiot/main/test.csv"
    dfspf = pd.read_csv(url)
    df1 = dfspf.values
    X = df1[:, 0:3]  # all rows and first two columns become my input ie. X
    Y = df1[:, 3]    # all rows and only third column become my output ie Y
    model2 = LogisticRegression()
    model2.fit(X, Y)
    arr = model2.predict([[sw, sh, pw]])
    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    month_name = month_names[sh - 1]
    return render_template("rain.html", sw=sw, sh=sh, pw=pw, month_name=month_name, data=str(arr[0]) + " mm")

# Function to convert month number to month name
@app.template_filter("get_month")
def get_month(month_number):
    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    return month_names[month_number - 1]

if __name__ == "__main__":
    app.run(debug=True)
    