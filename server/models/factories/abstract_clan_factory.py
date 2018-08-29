from abc import ABC, abstractmethod
from ..clans import Kuirk, Strolth, Ranger


class AbstractClanFactory(ABC):
    """
        AbstractClanFactory
    """

    @staticmethod
    @abstractmethod
    def get_race_sprite():
        pass

    @staticmethod
    @abstractmethod
    def get_ships():
        pass


class ConcreteStrolthFactory(AbstractClanFactory):

    @staticmethod
    def get_race_sprite():
        return Strolth()


class ConcreteRangerFactory(AbstractClanFactory):
    pass


class ConcreteKuirkFactory(AbstractClanFactory):
    pass
