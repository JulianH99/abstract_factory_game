from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO

from .models.factories.sprite_factories import ShipFactory
from .models.base  import Sprite, Player

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
    sprite = Player(gender)

    sprite.sprite_name = "My name"

    return sprite.get_json()


@socketio.on('message')
def connected():
    print("Connected with sokectio from webpage")
    socketio.emit("response")


if __name__ == '__main__':
    socketio.run(app)
