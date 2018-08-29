from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO

from .models.factories.sprite_factories import ShipFactory

app = Flask(__name__)

CORS(app=app)

# get socket io working
socketio = SocketIO(app)


@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/get_group_of/<gender>')
@cross_origin()
def get_group_of(gender: str):
    print(gender)


@socketio.on('message')
def connected():
    print("Connected with sokectio from webpage")
    socketio.emit("response")


if __name__ == '__main__':
    socketio.run(app)
