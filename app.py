from flask import Flask
from flask_pymongo import PyMongo
app = Flask(__name__)

@app.route('/')
def indes():
  return 'hello world'
