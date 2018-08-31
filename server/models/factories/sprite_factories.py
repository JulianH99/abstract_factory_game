from abc import ABC, abstractmethod
from random import choice
from string import ascii_letters
from ..base import Player
from ..ships import Ship, AgileShip, HeavyShip, SmartShip


class SpriteFactory(ABC):
    """
    Class spriteFactory
    """

    @staticmethod
    @abstractmethod
    def factory_method(self):
        pass


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
    def factory_method(ship_type, speed, resistance, attack) -> Ship:
        if ship_type == AgileShip.name:
            return AgileShip(speed, resistance, attack)
        elif ship_type == HeavyShip.name:
            return HeavyShip(speed, resistance, attack)
        elif ship_type == SmartShip.name:
            return SmartShip(speed, resistance, attack)
        else:
            raise Exception("{} is not a known ship type".format(ship_type))
