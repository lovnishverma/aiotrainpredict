#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template
import sqlite3

app = Flask(__name__, static_folder='public', template_folder='views')

conn = sqlite3.connect('example.db')
c = conn.cursor()

def table_exists (name):
  conn = sqlite3.connect('example.db')
  c = conn.cursor()
  cnt = c.execute('''SELECT COUNT(*) FROM sqlite_master 
                    WHERE type='table' AND name='{}';'''.format(name) )
  print("result" + str(cnt))
  
# Create table

c.execute('''CREATE TABLE IF NOT EXISTS stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()


@app.route('/')
def home():
    print("home")
    table_exists("stocks")
    table_exists("todos")
    return render_template('app.html', maker=os.environ.get("MADE_BY"))

if __name__ == '__main__':
    app.run()