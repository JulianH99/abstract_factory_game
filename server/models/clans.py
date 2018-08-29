from abc import ABCMeta, abstractmethod
from .base import Sprite
from typing import List, Dict
from .ships import Ship


class Clan(Sprite, metaclass=ABCMeta):
    __ships: List[Ship]
    __specialized_attributes: Dict[str, int]

    @abstractmethod
    def apply_attributes(self):
        pass

    @property
    def ships(self) -> List[Ship]:
        return self.__ships

    @ships.setter
    def ships(self, new_ships: List[ships]):
        self.__ships = new_ships

    @property
    def specialized_attributes(self) -> Dict[str, int]:
        return self.__specialized_attributes

    @specialized_attributes.setter
    def specialized_attributes(self, new_specialized_attributes: Dict[str, int]):
        self.__specialized_attributes = new_specialized_attributes


class Kuirk(Clan):
    pass


class Ranger(Clan):
    pass


class Strolth(Clan):
    pass