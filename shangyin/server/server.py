from flask import Flask, render_template
import threading
import time

dbref = None
cofcarduser_join = 'JOIN card on card_id=card.id JOIN user ON user_id=user.id'

class ServerRunner(threading.Thread):
    def run(self):
        app = Flask(__name__)

        @app.route("/")
        def overview():
            global dbref

            recent = dbref.select('coffee.id, card_id, logged, milk, user_id, fullname, department', 
                    'coffee', cofcarduser_join + ' ORDER BY logged DESC LIMIT 5'
                )

            counts = dbref.select('department, COUNT(department)', 'coffee',
                    cofcarduser_join + ' GROUP BY department'
                )

            return render_template('index.html', recent=recent, counts=counts)

        @app.route("/all")
        def all():
            global dbref

            data = dbref.select('coffee.id, card_id, logged, milk, user_id, fullname, department', 
                    'coffee', cofcarduser_join + ' ORDER BY logged DESC'
                )

            return render_template('all.html', logs=data)

        app.run(host='0.0.0.0', port=8000)

    def assign_db(self, db):
        global dbref
        dbref = db