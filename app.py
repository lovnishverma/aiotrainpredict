from flask import *  
import numpy   
import pandas  as pd 
from  sklearn.linear_model import LinearRegression 
from sklearn.linear_model import LogisticRegression
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
  
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/rainpredict')
def rainredict():
  return render_template("rain.html")

@app.route("/rainpredict", methods=["POST"])
def rainpredict():
  sw = eval ( request.form.get ( "sw") )
  sh = eval ( request.form.get ( "sh") )
  pw = eval ( request.form.get ( "pw") )
  url   = "https://raw.githubusercontent.com/priyanka9-99/aiot/main/test.csv"
  dfspf = pd.read_csv(url)
  df1   = dfspf.values
  X = df1[:,0:3] # all rows and first two columns  becomes my input ie. X
  Y = df1[:,3]   # all rows and only third column becomes my output ie Y 
  model2 = LogisticRegression ()
  model2.fit( X , Y )
  arr   = model2.predict([[sw, sh, pw]] )
  return render_template("rain.html" , data = str( arr[0] ) + " mm")

@app.route('/scrape_table_data')
def scrape_table_data():
    url = 'https://onlinenielitchandigarh.000webhostapp.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    rows = table.find_all('tr')
    latest_row = rows[1]  # Get the latest top row
    cells = latest_row.find_all('td')
    temperature = cells[1].text
    date_time = cells[0].text
    return temperature, date_time

@app.route('/')
def index():
    temperature, date_time = scrape_table_data()
    return render_template('temp.html', temperature=temperature, date_time=date_time)

if __name__ == "__main__":
  app.run(debug=True)