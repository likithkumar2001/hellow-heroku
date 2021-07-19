from flask import Flask
import db
app = Flask(__name__)

@app.route('/')
def indes():
  return 'hello world'

@app.route("/test")
def test():
  f=db.mydoc 
  x = "."
  for y in f:
    x=y
  return x
