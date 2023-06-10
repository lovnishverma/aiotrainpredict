from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/rainpredict')
def rainpredict():
    return render_template("rain.html")

@app.route("/rainpredict", methods=["POST"])
def predict_rainfall():
    sw = int(request.form.get("sw"))
    sh = int(request.form.get("sh"))
    pw = float(request.form.get("pw"))

    url = "https://raw.githubusercontent.com/priyanka9-99/aiot/main/test.csv"
    df = pd.read_csv(url)
    X = df.iloc[:, 0:3].values
    Y = df.iloc[:, 3].values

    model = LogisticRegression()
    model.fit(X, Y)

    predicted_rainfall = model.predict([[sw, sh, pw]])

    return render_template("rain.html", year=sw, month=sh, temperature=pw, rainfall=predicted_rainfall[0])

if __name__ == "__main__":
    app.run(debug=True)
    