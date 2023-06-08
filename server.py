from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/rain')
def about():
    return render_template("rain.html")

@app.route('/live_sensor_data')
def contact():
    return render_template("template.html")

if __name__ == '__main__':
    app.run()
