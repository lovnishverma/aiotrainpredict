from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LogisticRegression
import json
import requests
from fpdf import FPDF

API_KEY = "48b4ff1931msh5e006d4c3f36210p1b8d04jsn203e95aa9d55"
API_HOST = "weatherapi-com.p.rapidapi.com"
API_URL = "https://weatherapi-com.p.rapidapi.com/current.json"

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
        url = "https://raw.githubusercontent.com/lovnishverma/datasets/main/test.csv"
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

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/predict_weather',methods=['POST'])
def predict_weather():
    if request.method == 'POST':
        q = request.form['location']
        url = API_URL
        querystring = {"q":q}
        headers = {
            "X-RapidAPI-Key": API_KEY,
            "X-RapidAPI-Host": API_HOST
        }
        try:
            response = requests.request("GET", url, headers=headers, params=querystring)
            json_data = json.loads(response.text)
            
            name = json_data['location']['name']
            region = json_data['location']['region']
            country = json_data['location']['country']
            lat = json_data['location']['lat']
            lon = json_data['location']['lon']
            tz_id = json_data['location']['tz_id']
            localtime_epoch = json_data['location']['localtime_epoch']
            localtime = json_data['location']['localtime']
            last_updated_epoch = json_data['current']['last_updated_epoch']
            last_updated = json_data['current']['last_updated']
            temp_c = json_data['current']['temp_c']
            temp_f = json_data['current']['temp_f']
            is_day = json_data['current']['is_day']
            condition_text = json_data['current']['condition']['text']
            condition_icon = json_data['current']['condition']['icon']
            wind_mph = json_data['current']['wind_mph']
            wind_kph = json_data['current']['wind_kph']
            wind_degree = json_data['current']['wind_degree']
            wind_dir = json_data['current']['wind_dir']
            pressure_mb     = json_data['current']['pressure_mb']
            pressure_in = json_data['current']['pressure_in']
            precip_mm = json_data['current']['precip_mm']
            precip_in = json_data['current']['precip_in']
            humidity = json_data['current']['humidity']
            cloud = json_data['current']['cloud']
            feelslike_c = json_data['current']['feelslike_c']
            feelslike_f = json_data['current']['feelslike_f']
            vis_km = json_data['current']['vis_km']
            vis_miles = json_data['current']['vis_miles']
            uv = json_data['current']['uv']
            gust_mph = json_data['current']['gust_mph']
            gust_kph = json_data['current']['gust_kph']

            return render_template('home.html',name=name,region=region,country=country,lat=lat,lon=lon,tz_id=tz_id,
            localtime_epoch=localtime_epoch,localtime=localtime,last_updated_epoch=last_updated_epoch,last_updated=last_updated,
            temp_c=temp_c,temp_f=temp_f,is_day=is_day,condition_text=condition_text,condition_icon=condition_icon,wind_mph=wind_mph,
            wind_kph=wind_kph,wind_degree=wind_degree,wind_dir=wind_dir,pressure_mb=pressure_mb,pressure_in=pressure_in,precip_mm=precip_mm,
            precip_in=precip_in,humidity=humidity,cloud=cloud,feelslike_c=feelslike_c,feelslike_f=feelslike_f,vis_km=vis_km,
            vis_miles=vis_miles,uv=uv,gust_mph=gust_mph,gust_kph=gust_kph)

        except:
            return render_template('home.html',error='Please enter a correct Place name...')

@app.route('/livedata')
def display_data():
    # Specify the URL of your PHP page
    php_url = 'https://onlinenielitchandigarh.000webhostapp.com/glitch.php'

    # Make a GET request to the PHP URL
    response = requests.get(php_url)

    # Get the JSON data from the response
    data = response.json()

    # Render the template with the data
    return render_template('live.html', data=data)

#if __name__ == '__main__':
    #app.run()

if __name__ == '__main__':
    app.run(debug=True)