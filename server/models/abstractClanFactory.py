from abc import ABC, abstractmethod


class AbstractClanFactory(ABC):
    """
        AbstractClanFactory
    """

    def get_RaceSprite(self):
        pass

    def get_Ships(self):
        pass


class ConcreteStrolthFactory(abstractClanFactory):
    pass


class ConcreteRangerFactory(abstractClanFactory):
    pass


class ConcreteKuirkFactory(abstractClanFactory):
    pass
