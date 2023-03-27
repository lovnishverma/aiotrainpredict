
from flask import *  
import sqlite3
import numpy   
import pandas  as pd 
from  sklearn.linear_model import LinearRegression 

app = Flask(__name__)

#   install following in glitch terminal 
# pip install scikit-learn
# pip install pandas

@app.route("/ml")
def machinelearning():
  url  = "https://raw.githubusercontent.com/sarwansingh/Python/master/ClassExamples/data/student-pass-fail-data.csv"
  dfspf = pd.read_csv(url)
  df1 = dfspf.values
  X = df1[:,0:2]
  Y = df1[:,2]
  model = LinearRegression ()
  model.fit( X , Y )
  arr = model.predict([[3,35]] )
  return "Prediction  :  " + str(arr[0])
  #dfspf.head()

@app.route('/')
def defaultroot():
  #get the data from database - db1 and table - students
  con  = sqlite3.connect("db1")  # connect sms database
  con.row_factory = sqlite3.Row  # create object of Row
  cur = con.cursor()             
  cur.execute( "select * from students")  # execute a SQL query to get the data
  rows = cur.fetchall()          # all the data pulled from database is stored in rows object 
  con.close ()
  
  return render_template("index.html", data=rows)

if __name__ == '__main__':
  app.run()
  
'''
CREATE TABLE students
             (studentid integer  primary key AUTOINCREMENT,
              name varchar(30) NOT NULL,
              email varchar(40) NOT NULL,
              passwd varchar(20) NOT NULL) ;
insert into students ( name, email, passwd) values ('Ram' , 'ram@gmail.com','rr') ;           
insert into students ( name, email, passwd) values ('Sita', 'sita@gmail.com','ss');             
'''