from flask import Flask,request
from flask_pymongo import pymongo
import urllib
import dns
app = Flask(__name__)

def connection():
  CONNECTION_STRING = 'mongodb+srv://likith:' + urllib.parse.quote("Rp-iA@c6!Nq45c4") + '@cluster0.ms0ap.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
  client = pymongo.MongoClient(CONNECTION_STRING)
  base = client.weather
  data = base.data
  client.close()
  return data

def fnd(x):
  data = connection();
  mydoc = data.find(x)
  x = "."
  for y in mydoc:
    x=y
  return x

@app.route("/")
def home():
  return 'Welcome change the url by adding /data_for?place=NAME !!!'

@app.route("/data_for")
def place():
  plc = request.args.get("place")
  x = {'title': plc}
  val = fnd(x)
  IST = pytz.timezone('Asia/Kolkata')
  now = datetime.now(IST)
  current_time = now.strftime("%H.%M")
  if  val['Valid upto'] <= float(current_time):
    u = data_accumulation.web_scrapping();
    info = data_accumulation.data_cleaning(u);
    data_accumulation.store_data(info);
  x = {'title': plc}
  x = {'title': result}
  val = fnd(x)
  return val['Message']
  


    

