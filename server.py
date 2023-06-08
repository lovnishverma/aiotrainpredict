from flask import *  
import sqlite3
import numpy   
import pandas  as pd 
from  sklearn.linear_model import LinearRegression 
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

#   install following in glitch terminal 
# pip install scikit-learn
# pip install pandas
@app.route('/')
def rainpage():
  return render_template("rain.html")

@app.route("/rain", methods=["POST"])
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
  # return "Rain Prediction   :  " + str(arr[0] ) + " mm"


@app.route('/irisp' , methods=["POST"])
def irispredict():
  sw = eval ( request.form.get ( "sw") )
  sh = eval ( request.form.get ( "sh") )
  pw = eval ( request.form.get ( "pw") )
  ph = eval ( request.form.get ( "ph") )
  ######### machine learning
  url ="https://raw.githubusercontent.com/sarwansingh/Python/master/ClassExamples/data/iris.csv"
  #nameslist = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']
  dfIris =  pd.read_csv(url, header=None ) # , names=nameslist)
  df2 = dfIris.values
  
  #divide data into feature matrix and target matrix
  X = df2[:,:4] # all the rows and first four columns 0-3
  Y = df2[:,4]   # all the rows and only fourth column (last column )
  
  from sklearn.linear_model import LogisticRegression
  model1= LogisticRegression()
  model1.fit(X,Y)
  arr  = model1.predict([[ sw, sh, pw, ph]])
  ###############
  return render_template("iris.html" , data = str( arr[0] ) )


@app.route("/p", methods=["POST"])
def predictresult():
  hrsself = int ( request.form.get ( "hrsself") )
  hrstut  = int ( request.form.get ( "hrstut") ) 
  # predict and save the output in result variable
  url   = "https://raw.githubusercontent.com/sarwansingh/Python/master/ClassExamples/data/student-pass-fail-data.csv"
  dfspf = pd.read_csv(url)
  df1   = dfspf.values
  X = df1[:,0:2] # all rows and first two columns  becomes my input ie. X
  Y = df1[:,2]   # all rows and only third column becomes my output ie Y 
  model = LinearRegression ()
  model.fit( X , Y )
  arr   = model.predict([[hrsself,hrstut]] )
  #################
  result = arr[0] *100
  return render_template("result.html", data = str(result) + "%")

@app.route("/ml")
def machinelearning():
  url   = "https://raw.githubusercontent.com/sarwansingh/Python/master/ClassExamples/data/student-pass-fail-data.csv"
  dfspf = pd.read_csv(url)
  df1   = dfspf.values
  X = df1[:,0:2] # all rows and first two columns  becomes my input ie. X
  Y = df1[:,2]   # all rows and only third column becomes my output ie Y 
  model = LinearRegression ()
  model.fit( X , Y )
  arr   = model.predict([[5,25]] )
  return "Passing Prediction   :  " + str(arr[0] * 100) + "%"

  
  return render_template("index.html", data=rows)

if __name__ == '__main__':
  app.run()
  