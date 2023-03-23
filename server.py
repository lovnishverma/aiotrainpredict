from flask import *  

app = Flask(__name__)

@app.route('/')
def defaultroot():
  return 'Hello, World!'

if __name__ == '__main__':
  app.run()
  
'''
CREATE TABLE students
             (studentid integer  primary key AUTOINCREMENT,
              name varchar(30) NOT NULL,
              email varchar(40) NOT NULL,
              passwd varchar(20) NOT NULL) ;
 insert into students ( name, email, passwd) values (  'Ram' , 'ram@gmail.com','rr')            
              
'''