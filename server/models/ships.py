from abc import ABCMeta
from .base import Sprite
from typing import List


class Ship(Sprite, metaclass=ABCMeta):
    __speed: int
    __resistance: int
    __attack: int
    __accessories: List[object]

    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, new_speed: int):
        self.__speed = new_speed

    @property
    def resistance(self) -> int:
        return self.__resistance

    @resistance.setter
    def resistance(self, new_resistance: int):
        self.__resistance = new_resistance

    @property
    def attack(self) -> int:
        return self.__attack

    @attack.setter
    def attack(self, new_attack: int):
        self.__resistance = new_attack

    @property
    def accessories(self) -> List[object]:
        return self.__accessories

    @accessories.setter
    def accessories(self, new_accessories: List[object]):
        self.__accessories = new_accessories


class AgileShip(Ship):
    pass


class HeavyShip(Ship):
    pass


class SmartShip(Ship):
    pass
