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
            logs = map(lambda x: 'ID {}, CARD {}, TIME {}'.format(x[0], x[1], x[2]), data)

            return render_template('index.html', logs=logs)

        app.run(host='0.0.0.0', port=8000, debug=True, use_reloader=False)

    def assign_db(self, db):
        global dbref
        dbref = db