from abc import ABCMeta, abstractmethod

from flask import jsonify

from .base import Sprite
from typing import List, Dict
from .ships import Ship


class Clan(Sprite, metaclass=ABCMeta):
    _ships: List[Ship]
    _specialized_attributes: Dict[str, Dict[str, int]]
    name: str

    def __init__(self, specialized_attributes: Dict[str, Dict[str, int]]):
        self._specialized_attributes = specialized_attributes

    @property
    def ships(self) -> List[Ship]:
        return self._ships

    @ships.setter
    def ships(self, new_ships: List[Ship]):
        self._ships = new_ships

    @property
    def specialized_attributes(self) -> Dict[str, Dict[str, int]]:
        return self._specialized_attributes

    @specialized_attributes.setter
    def specialized_attributes(self, new_specialized_attributes: Dict[str, Dict[str, int]]):
        self._specialized_attributes = new_specialized_attributes

    def get_json(self):
        name = self.name
        id = self.id

        return {"name": name, "id": id}


class Kuirk(Clan):
    """
    Specialized in driving the AgileShip
    """

    name = "kuirk"
    
    def __init__(self):
        specialized_attributes = {
            "heavy": {
                "speed": 50,
                "resistance": 70,
                "attack": 65
            },
            "agile": {
                "speed": 80,
                "resistance": 60,
                "attack": 80
            },
            "smart": {
                "speed": 70,
                "resistance": 60,
                "attack": 70
            },
        }

        self.specialized_attributes = specialized_attributes


class Ranger(Clan):
    """
    Specialized in driving the SmartShip
    """
    name = "ranger"

    def __init__(self):
        specialized_attributes = {
            "heavy": {
                "speed": 50,
                "resistance": 70,
                "attack": 70
            },
            "agile": {
                "speed": 70,
                "resistance": 50,
                "attack": 70
            },
            "smart": {
                "speed": 80,
                "resistance": 70,
                "attack": 90
            },
        }

        self.specialized_attributes = specialized_attributes


class Strolth(Clan):
    """
    Specialized in driving the HeavyShip
    """
    
    name = "strolth"

    def __init__(self):
        specialized_attributes = {
            "heavy": {
                "speed": 60,
                "resistance": 80,
                "attack": 75
            },
            "agile": {
                "speed": 60,
                "resistance": 50,
                "attack": 65
            },
            "smart": {
                "speed": 60,
                "resistance": 60,
                "attack": 70
            },
        }

        self.specialized_attributes = specialized_attributes

