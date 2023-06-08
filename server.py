from flask import *
import pandas as pd
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/rain')
def rain_page():
    return render_template("rain.html")

@app.route('/rain', methods=["POST"])
def predict_rain():
    sw = float(request.form.get("sw"))
    sh = float(request.form.get("sh"))
    pw = float(request.form.get("pw"))
    
    url = "https://raw.githubusercontent.com/priyanka9-99/aiot/main/test.csv"
    df = pd.read_csv(url)
    X = df.iloc[:, 0:3].values  # Input features
    Y = df.iloc[:, 3].values    # Output variable

    model = LogisticRegression()
    model.fit(X, Y)
    
    rainfall_prediction = model.predict([[sw, sh, pw]])[0]
    
    return render_template("rain.html", rainfall=rainfall_prediction)

if __name__ == '__main__':
    app.run()
