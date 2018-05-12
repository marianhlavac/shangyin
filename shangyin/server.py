import threading
import time
import http.server

dbref = None

class Server(http.server.BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        global dbref
        self._set_headers()

        data = dbref.select('*', 'coffee')

        coffees = '<br>'.join(map(lambda x: 'ID {}, CARD {}, TIME {}'.format(x[0], x[1], x[2]), data))

        content = '<html><body><h1>Server test</h1><p>{}</p></body></html>'.format(coffees)
        self.wfile.write(content.encode())

    def do_HEAD(self):
        self._set_headers()

class ServerRunner(threading.Thread):
    def run(self):
        server_address = ('', 8000) #FIXME: parametrize
        httpd = http.server.HTTPServer(server_address, Server)
        httpd.serve_forever()

    def assign_db(self, db):
        global dbref
        dbref = db