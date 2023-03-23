from flask import *  
import sqlite3

app = Flask(__name__)

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