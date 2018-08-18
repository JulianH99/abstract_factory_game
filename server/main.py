from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
CORS(app)

# get socket io working
socketio = SocketIO(app)

@app.route('/')
def hello_world():
    return 'hello world'

@socketio.on('connected')
def connected():
    print("Connected with sokectio from webpage")

if __name__ == '__main__':
    socketio.run(app)