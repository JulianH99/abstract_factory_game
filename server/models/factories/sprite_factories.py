from abc import ABC, abstractmethod
from ..clans import Kuirk, Ranger, Strolth, Clan
from ..base import Player
from ..ships import Ship, AgileShip, HeavyShip, SmartShip
from .abstract_clan_factory import AbstractClanFactory, \
ConcreteKuirkFactory,\
 ConcreteRangerFactory,\
  ConcreteStrolthFactory


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
    def factory_method(clan) -> AbstractClanFactory:
        if clan == Kuirk.name:
            return ConcreteKuirkFactory()
        elif clan == Strolth.name:
            return ConcreteStrolthFactory()
        elif clan == Ranger.name:
            return ConcreteRangerFactory()
        else:
            raise Exception("{} is not a known clan type".format(clan))



class PlayerFactory(SpriteFactory):
    """
        class PlayerFactory
    """

    @staticmethod
    def factory_method(gender) -> Player:
        pass


class ShipFactory(SpriteFactory):
    """
        class ShipFactory
    """

    @staticmethod
    def factory_method(ship_type) -> Ship:
        if ship_type == 'AgileShip':
            return AgileShip()
        elif ship_type == 'HeavyShip':
            return HeavyShip()
        elif ship_type == 'SmartShip':
            return SmartShip()
        else:
            raise Exception("{} is not a known ship type".format(ship_type))