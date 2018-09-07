from abc import ABC, abstractmethod
from random import choice, randint
from string import ascii_letters
from ..base import Player, Pirate
from ..ships import Ship, AgileShip, HeavyShip, SmartShip


class SpriteFactory(ABC):
    """
    Class spriteFactory
    """

    @staticmethod
    @abstractmethod
    def factory_method():
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

    @classmethod
    def random_ship(cls) -> Ship:
        ships = [AgileShip.name, HeavyShip.name, SmartShip.name]
        attack = randint(10, 70)
        speed = randint(10, 70)
        resistance = randint(10, 70)
        ship = choice(ships)

        return cls.factory_method(ship_type=ship,
                                  speed=speed,
                                  attack=attack,
                                  resistance=resistance)

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


class PirateFactory(SpriteFactory):
    """
    class Pirate Factory
    """
    @staticmethod
    def factory_method():
        ship = ShipFactory.random_ship()
        pirate = Pirate()

        pirate.ship = ship

        return pirate
