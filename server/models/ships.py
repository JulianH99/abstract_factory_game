from abc import ABC
from .base import Sprite
from typing import List


class Ship(ABC, Sprite):
    __speed: int
    __resistance: int
    __attack: int
    __accessories: List[object]


class AgileShip(Ship):
    pass


class HeavyShip(Ship):
    pass


class SmartShip(Ship):
    pass
