import os
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
  host = os.environ.get('HOSTNAME')
  print(f'host: {host}')
  return render_template("index.html", host=host)

if __name__ == "__main__":
  port = int(os.environ.get('PORT', 5000))
  app.run(debug=True, host='0.0.0.0', port=port)
