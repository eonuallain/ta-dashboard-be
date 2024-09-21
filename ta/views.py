"""Text analysis views"""

import os
import pika

from flask import jsonify
from flask import request, render_template

from ta import app
from ta import db
from ta import model as models

@app.route('/')
def index():
    """The index page handler"""
    hostname = os.environ.get('HOSTNAME')
    if hostname is None:
        hostname = os.environ.get('HOST')
    
    #entries = models.TextEntry.query.all()
    entry_count = models.TextEntry.query.count()
    return render_template("index.html", host=hostname, count=entry_count)


@app.route('/postmessage', methods=['POST'])
def post_message():
    """Handle new posted message"""

    try:
        print(f"post_message() called with request: {request}")
        data = request.form

        print(data.keys())
        print(data.values())

        if data['message'] is not None:
            body = data['message'].strip()
        else:
            body = str(data)

        body_len = len(body)
        print(f"post_message() body: [{body_len}] {body}")

        if body_len == 0:
            print(f"post_message() not posting as message length is {body_len}")
            status = {"status" : "failure"}
        else:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='localhost')
            )

            channel = connection.channel()
            channel.queue_declare(queue='hello')
            channel.basic_publish(exchange='', routing_key='hello', body=body)

            print("post_message() done")
            connection.close()
            status = {"status" : "success"}
    except Exception as e:
        print(e)
        status = {"status" : "failure", "error" : str(e)}

    return jsonify(status)
