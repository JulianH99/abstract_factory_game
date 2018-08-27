from abc import ABC, abstractmethod


class AbstractClanFactory(ABC):
    """
        AbstractClanFactory
    """

    @staticmethod
    @abstractmethod
    def get_race_sprite(self):
        pass

    @staticmethod
    @abstractmethod
    def get_ships(self):
        pass


class ConcreteStrolthFactory(AbstractClanFactory):
    pass


class ConcreteRangerFactory(AbstractClanFactory):
    pass


class ConcreteKuirkFactory(AbstractClanFactory):
    pass
