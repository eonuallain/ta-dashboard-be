"""Text analysis"""

from flask import Flask

app = Flask(__name__)

#pylint: disable=wrong-import-position
import ta.views
