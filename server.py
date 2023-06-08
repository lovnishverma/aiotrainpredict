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


if __name__ == '__main__':
    app.run()
