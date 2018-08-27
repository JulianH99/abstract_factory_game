from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

from models.factories.sprite_factories import ShipFactory


app = Flask(__name__)
CORS(app)

# get socket io working
socketio = SocketIO(app)

ship = ShipFactory()

ship.factory_method('mytype')


@app.route('/')
def hello_world():
    return 'hello world'


@socketio.on('message')
def connected():
    print("Connected with sokectio from webpage")
    socketio.emit("response")


if __name__ == '__main__':
    socketio.run(app)
