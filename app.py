from flask import Flask,request
from flask_pymongo import pymongo
import urllib
import dns
from datetime import datetime
import data_accumulation
import pytz
import pandas as pd
from translate import Translator
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
  z = "."
  for y in mydoc:
    z=y
  return z

@app.route("/")
def home():
  
  return 'Welcome change the url by adding /data_for?place=NAME !!!'

@app.route("/data_for")
def place():
  plc = request.args.get("place").upper()
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
  val = fnd(x)
  df = pd.read_csv("./AP&TEL.csv")[['NAME_2','lang']]
  dic = {}
  for i in range(len(df['NAME_2'])):
    dic[df['NAME_2'][i].upper()] = df['lang'][i]

  translator = Translator(to_lang=dic[plc])
  xyz = translator.translate(val['Message'])
  return xyz

@app.route("/pdf")
def pdf():
  url = "https://mausam.imd.gov.in/imd_latest/contents/agromet/agromet-data/district/current/english-pdf/Anantpur.pdf"
  filedata = urllib.request.urlopen(url)
  datatowrite = filedata.read()
  try:
    with open('data.pdf', 'wb') as f:
      f.write(datatowrite)
    filedata.close()
  except:
    filedata.close()
    return "not done"

  


    

