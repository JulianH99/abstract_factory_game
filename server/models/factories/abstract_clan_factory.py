from abc import ABC, abstractmethod
from ..clans import Kuirk, Strolth, Ranger
from ..ships import Ship, SmartShip, HeavyShip, AgileShip


class AbstractClanFactory(ABC):
    """
        AbstractClanFactory
    """

    @staticmethod
    @abstractmethod
    def get_race_sprite(gender: str):
        pass

    @staticmethod
    @abstractmethod
    def get_ships():
        pass


class ConcreteStrolthFactory(AbstractClanFactory):

    @staticmethod
    def get_race_sprite(gender: str):
        return Strolth()

    @staticmethod
    def get_ships():
        return [AgileShip(), HeavyShip(), SmartShip()]


class ConcreteRangerFactory(AbstractClanFactory):

    @staticmethod
    def get_race_sprite():
        return Ranger()

    @staticmethod
    def get_ships():
        return [AgileShip(), HeavyShip(), SmartShip()]


class ConcreteKuirkFactory(AbstractClanFactory):

    @staticmethod
    def get_race_sprite():
        return Kuirk()

    @staticmethod
    def get_ships():
        return [AgileShip(), HeavyShip(), SmartShip()]