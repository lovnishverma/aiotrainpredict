#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__, static_folder='public', template_folder='views')

@app.route('/')
def home():
    return render_template('app.html')

if __name__ == '__main__':
    app.run()