from flask import Flask,request
from flask_pymongo import pymongo
import urllib
import dns
app = Flask(__name__)

CONNECTION_STRING = 'mongodb+srv://likith:' + urllib.parse.quote("Rp-iA@c6!Nq45c4") + '@cluster0.ms0ap.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
client = pymongo.MongoClient(CONNECTION_STRING)
base = client.weather
data = base.data
@app.route("/")
def home():
  return 'Connected to MONGODB!!!'
@app.route("/data_for")
def place():
  plc = request.args.get("place")
  x = {'title': plc}
  mydoc = data.find(x) 
  x = "."
  for y in mydoc:
    x=y
  return x['Message']
  


    

