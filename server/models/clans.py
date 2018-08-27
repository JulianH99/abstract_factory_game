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


class Kuirk(Clan):
    pass


class Ranger(Clan):
    pass


class Strolth(Clan):
    pass
