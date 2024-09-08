#import os

#from flask import render_template

#@app.route("/")
#def home():
#  host = os.environ.get('HOSTNAME')
#  print(f'host: {host}')
#  return render_template("index.html", host=host)




import os

from flask import render_template
from ta import app

@app.route('/')
def index():
  host = os.environ.get('HOSTNAME')
  print(f'host: {host}')
  return render_template("index.html", host=host)