from abc import ABC, abstractmethod
from ..clans import Kuirk, Ranger, Strolth, Clan
from ..base import Player
from ..ships import Ship
from .abstract_clan_factory import AbstractClanFactory


class SpriteFactory(ABC):
    """
    Class spriteFactory
    """

    @staticmethod
    @abstractmethod
    def factory_method(self):
        pass


class FactoryClanAbsFact(SpriteFactory):
    """
        class FactoryClanAbsFact
    """

    @staticmethod
    def factory_method(self, clan) -> AbstractClanFactory:
        pass


class PlayerFactory(SpriteFactory):
    """
        class PlayerFactory
    """

    @staticmethod
    def factory_method(self, gender) -> Player:
        pass


class ShipFactory(SpriteFactory):
    """
        class ShipFactory
    """
    def factory_method(self, ship_type) -> Ship:
        pass
