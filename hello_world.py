"""Filename: hello-world.py
"""

from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
def hello_world(username=None):
    
    return("Hello {}!".format(username))
