from flask import *
import numpy
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/rainpredict')
def rainredict():
    return render_template("rain.html")

@app.route("/rainpredict", methods=["POST"])
def rainpredict():
    sw = eval(request.form.get("sw"))
    sh = eval(request.form.get("sh"))
    pw = eval(request.form.get("pw"))

    url = "https://raw.githubusercontent.com/priyanka9-99/aiot/main/test.csv"
    dfspf = pd.read_csv(url)
    df1 = dfspf.values
    X = df1[:, 0:3]
    Y = df1[:, 3]

    model2 = LogisticRegression()
    model2.fit(X, Y)

    arr = model2.predict([[sw, sh, pw]])

    return render_template("rain.html", sw=sw, sh=sh, pw=pw, data=str(arr[0]) + " mm")

if __name__ == "__main__":
    app.run(debug=True)
    