from abc import ABCMeta
from flask import jsonify
from .base import Sprite
from typing import List


class Ship(Sprite, metaclass=ABCMeta):
    _speed: int
    _resistance: int
    _attack: int
    _accessories: List[object]
    name = ''

    def __init__(self, speed, resistance, attack):
        self._speed= speed
        self._resistance = resistance
        self._attack = attack

    @property
    def speed(self) -> int:
        return self._speed

    @speed.setter
    def speed(self, new_speed: int):
        self._speed = new_speed

    @property
    def resistance(self) -> int:
        return self._resistance

    @resistance.setter
    def resistance(self, new_resistance: int):
        self._resistance = new_resistance

    @property
    def attack(self) -> int:
        return self._attack

    @attack.setter
    def attack(self, new_attack: int):
        self._resistance = new_attack

    @property
    def accessories(self) -> List[object]:
        return self._accessories

    @accessories.setter
    def accessories(self, new_accessories: List[object]):
        self._accessories = new_accessories

    def get_json(self):
        json_dict = super().get_json()
        json_dict['speed'] = self.speed
        json_dict['resistance'] = self.resistance
        json_dict['attack'] = self.attack
        json_dict['accesories'] = None

        return json_dict


class AgileShip(Ship):
    name = 'agile'
    pass


class HeavyShip(Ship):
    name = 'heavy'
    pass


class SmartShip(Ship):
    name = 'smart'
    pass
