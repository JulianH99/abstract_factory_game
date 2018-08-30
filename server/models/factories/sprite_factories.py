from abc import ABC, abstractmethod
from random import randint, choice
from string import ascii_letters
from ..clans import Kuirk, Ranger, Strolth, Clan
from ..base import Player
from ..ships import Ship
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
        player = Player(gender)
        
        player.sprite_name = "".join(choice(ascii_letters) for x in range(6))

        return player


class ShipFactory(SpriteFactory):
    """
        class ShipFactory
    """

    @staticmethod
    def factory_method(ship_type) -> Ship:
        pass
