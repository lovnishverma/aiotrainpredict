#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template
import pymongo
import json
from bson import json_util

app = Flask(__name__, static_folder='public', template_folder='views')

def fill_collection (todos):
    todos.insert_one({"id": 1, "todo": "Boodschappen"})
    todos.insert_one({"id": 2, "todo": "Geld halen"})
    todos.insert_one({"id": 3, "todo": "Boek lezen"})   

@app.route('/createdb')
def createdb(data):
    todo = json_util.loads(data) # convert from JSON format
  
    mongo_url = os.environ.get("MONGO_URL")
    client = pymongo.MongoClient(mongo_url) ## /demodb???
    db = client['demodb']
    
    #db = client.demodb
    
    
@app.route('/todo')
def new_todo(data):
    todo = json_util.loads(data) # convert from JSON format
  
    mongo_url = os.environ.get("MONGO_URL")
    client = pymongo.MongoClient(mongo_url) ## /demodb???
    db = client.demodb
    todos = db.todos
    
    todos.insert_one(todo)
    
    
    return "OK"
    
    
@app.route('/todos')
def get_todos():
    mongo_url = os.environ.get("MONGO_URL")
    client = pymongo.MongoClient(mongo_url) ## /demodb???
    
    todos = client.demodb.todos
    if todos.count_documents({}) == 0:
        fill_collection(todos)
    todolist = list(todos.find())
    print(json_util.dumps(todolist))
    client.close()
    return json_util.dumps(todolist)
    
@app.route('/')
def home():
    print("home")
    return render_template('app.html', maker=os.environ.get("MADE_BY"))

if __name__ == '__main__':
    app.run()