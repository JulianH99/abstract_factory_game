from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO
from .models.factories.abstract_clan_factory import FactoryClanAbsFact

app = Flask(__name__)

CORS(app=app)

# get socket io working
socketio = SocketIO(app)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/get_group_of/<gender>/<clan>')
@cross_origin()
def get_group_of(gender: str, clan: str):
    clan_factory = FactoryClanAbsFact.factory_method(clan)

    clan = clan_factory.get_clan_sprite()

    player = clan_factory.get_player_sprite(gender)

    ship1, ship2, ship3 = clan_factory.get_ships()

    return jsonify(clan=clan.get_json())


@socketio.on('message')
def connected():
    print("Connected with sokectio from webpage")
    socketio.emit("response")


if __name__ == '__main__':
    socketio.run(app)
