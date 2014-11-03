#import modules
from flask import Flask, render_template
from flask_sockets import Sockets
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
sockets = Sockets(app)
app.wsgi_app = ProxyFix(app.wsgi_app)

@sockets.route('/echo')
def echo_socket(ws):
    while True:
        message = ws.receive()
        ws.send(message)

@app.route('/')
def hello():
    return render_template('index.html')

if __name__=="__main__":
	app.run()