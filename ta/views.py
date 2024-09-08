"""Text analysis views"""

import os

from flask import render_template
from ta import app

@app.route('/')
def index():
    """The index page handler"""
    host = os.environ.get('HOSTNAME')
    print(f'host: {host}')
    return render_template("index.html", host=host)
