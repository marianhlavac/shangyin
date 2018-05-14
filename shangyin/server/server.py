from flask import Flask, render_template
import threading
import time

dbref = None

class ServerRunner(threading.Thread):
    def run(self):
        app = Flask(__name__)

        @app.route("/")
        def hello():
            global dbref

            data = dbref.select('*', 'coffee')

            return render_template('index.html', logs=data)

        app.run(host='0.0.0.0', port=8000)

    def assign_db(self, db):
        global dbref
        dbref = db