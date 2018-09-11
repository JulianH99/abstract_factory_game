from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO
from .models.factories.abstract_clan_factory import FactoryClanAbsFact
from .models.prototypes import PiratePrototype
from .models.builders.directors import PlayerGroup
from .models.builders.base_builders import PlayerBuilder

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

    return jsonify(clan=clan.get_json(),
                   player=player.get_json(),
                   ship1=ship1.get_json(),
                   ship2=ship2.get_json(),
                   ship3=ship3.get_json())


@app.route('/get_pirates/<number>')
@cross_origin()
def get_pirates(number):
    number = int(number)
    pirates = [PiratePrototype.clone() for _ in range(number)]

    return jsonify([p.get_json() for p in pirates])


@app.route('/get_player_builder/<gender>/<clan>')
@cross_origin()
def get_player_builder(gender, clan):
    player_group = PlayerGroup(PlayerBuilder())

    player = player_group.build_player(gender, clan)
    return jsonify(
        player[0].get_json(),
        player[1].get_json()
    )


@socketio.on('message')
def connected():
    print("Connected with sokectio from webpage")
    socketio.emit("response")


if __name__ == '__main__':
    socketio.run(app)
