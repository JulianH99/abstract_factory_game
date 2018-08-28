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
    def accesories(self) -> List[object]:
        return self.__accesories

    @accesories.setter
    def accesories(self, new_accesories: List[object]):
        self.__accesories = new_accesories


class AgileShip(Ship):
    pass


class HeavyShip(Ship):
    pass


class SmartShip(Ship):
    pass
