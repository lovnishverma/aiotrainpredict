from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rainpredict')
def rainpredict():
    return render_template('rain.html')

@app.route('/rain', methods=['POST'])
def rain():
    if request.method == 'POST':
        # Retrieve form inputs
        year = int(request.form['sw'])
        month = int(request.form['sh'])
        temperature = float(request.form['pw'])

        # Load the rainfall prediction model
        url = "https://raw.githubusercontent.com/priyanka9-99/aiot/main/test.csv"
        df = pd.read_csv(url)
        X = df.iloc[:, 0:3]  # Select input features (year, month, temperature)
        Y = df.iloc[:, 3]  # Select target variable (rainfall)
        model = LogisticRegression()
        model.fit(X, Y)

        # Perform rainfall prediction
        rainfall = model.predict([[year, month, temperature]])

       # Render the result in rain.html template
        return render_template('rain.html', year=year, month=month, temperature=temperature, rainfall=str (rainfall[0]))
    
    return render_template('rain.html')

if __name__ == '__main__':
    app.run(debug=True)