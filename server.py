#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template

app = Flask(__name__, static_folder='public', template_folder='views')

@app.route('/')
def home():
    print("made by " + os.environ.get("MADE_BY"))
    return render_template('app.html', name=os.environ.get("MADE_BY"))

if __name__ == '__main__':
    app.run()