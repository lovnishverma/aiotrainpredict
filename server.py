#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template
import pymongo

app = Flask(__name__, static_folder='public', template_folder='views')

def fill_collection (todos):
    todos.insert_one({"id": 1, "todo": "Boodschappen"})
    todos.insert_one({"id": 2, "todo": "Geld halen"})
    todos.insert_one({"id": 3, "todo": "Boek lezen"})   

@app.route('/')
def home():
    print("home")
    mongo_url = os.environ["MONGO_URL"]
    mongo_port = 
    client = pymongo.MongoClient(, 63354) ## /demodb???
    db = client.demodb
    todos = db.todos
    
    if todos.count_documents({}) == 0:
      fill_collection(todos)

    res = list(todos.find()) ## list of all todo's
    print("result: " + str(res))

    client.close()
    return render_template('app.html', maker=os.environ.get("MADE_BY"), todos=res)

if __name__ == '__main__':
    app.run()