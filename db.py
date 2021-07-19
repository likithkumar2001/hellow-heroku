from flask import Flask
from flask_pymongo import pymongo
import urllib
import dns
CONNECTION_STRING = 'mongodb+srv://likith:' + urllib.parse.quote("Rp-iA@c6!Nq45c4") + '@cluster0.ms0ap.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
client = pymongo.MongoClient(CONNECTION_STRING)
base = client.weather
data = base.data
x = {'title': 'TINSUKIA'}
mydoc = data.find(x)

