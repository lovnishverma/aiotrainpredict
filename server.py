#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template
import sqlite3

app = Flask(__name__, static_folder='public', template_folder='views')

conn = sqlite3.connect('example.db')
c = conn.cursor()

def table_exists (cursor, name):
  cursor.execute('''SELECT name FROM sqlite_master 
                    WHERE type='table' AND name='{}';'''.format(name) )
  res = cursor.fetchall()
  print("res: " + str(res))
  print("result: " + str(len(res)))
  return len(res) > 0
  
# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()


@app.route('/')
def home():
    print("home")
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    if not table_exists(c, "todos"):
      c.execute('''CREATE TABLE IF NOT EXISTS todos 
                   (id int, todo text)''')
      c.execute('''INSERT INTO todos VALUES ("Boodschappen");''')
      c.execute('''INSERT INTO todos VALUES ("Geld halen");''')
      c.execute('''INSERT INTO todos VALUES ("Boek lezen");''')

    
    c.execute('''SELECT rowid, todo FROM todos''')
    res = c.fetchall()
    print("result: " + str(res))
    todos = []
    for todo in res:
      todos.append({"id": todo[0], "todo": todo[1]})
    print(str(todos))              
    conn.commit()
    conn.close()
    return render_template('app.html', maker=os.environ.get("MADE_BY"), todos=todos)

if __name__ == '__main__':
    app.run()