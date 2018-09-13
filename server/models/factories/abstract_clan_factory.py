from abc import ABC, abstractmethod
from ..clans import Kuirk, Strolth, Ranger
from ..ships import Ship, SmartShip, HeavyShip, AgileShip
from .sprite_factories import PlayerFactory, ShipFactory, SpriteFactory


class AbstractClanFactory(ABC):
    """
        AbstractClanFactory
    """

    @classmethod
    def get_player_sprite(cls, gender: str):
        player = PlayerFactory.factory_method(gender)

        if gender == 'male':
            gender_long = "Man"
        else:
            gender_long = "Woman"

        player.complete_sprite = "{}{}".format(gender_long, cls.get_clan_sprite().name.capitalize())
        return player

    @classmethod
    @abstractmethod
    def get_clan_sprite(cls):
        pass

    @classmethod
    def get_ships(cls):
        clan = cls.get_clan_sprite()

        specialized_attributes = clan.specialized_attributes
        agile_attributes = specialized_attributes['agile']
        heavy_attributes = specialized_attributes['heavy']
        smart_attributes = specialized_attributes['smart']

        heavy_ship = ShipFactory.factory_method(HeavyShip.name,
                                                heavy_attributes['speed'],
                                                heavy_attributes['resistance'],
                                                heavy_attributes['attack']
                                                )

        agile_ship = ShipFactory.factory_method(AgileShip.name,
                                                agile_attributes['speed'],
                                                agile_attributes['resistance'],
                                                agile_attributes['attack']
                                                )

        smart_ship = ShipFactory.factory_method(SmartShip.name,
                                                smart_attributes['speed'],
                                                smart_attributes['resistance'],
                                                smart_attributes['attack']
                                                )

        return agile_ship, heavy_ship, smart_ship


class ConcreteStrolthFactory(AbstractClanFactory):

    @classmethod
    def get_clan_sprite(cls):
        return Strolth()


class ConcreteRangerFactory(AbstractClanFactory):

    @classmethod
    def get_clan_sprite(cls):
        return Ranger()


class ConcreteKuirkFactory(AbstractClanFactory):

    @classmethod
    def get_clan_sprite(cls):
        return Kuirk()


class FactoryClanAbsFact(SpriteFactory):
    """
        class FactoryClanAbsFact
    """

    @staticmethod
    def factory_method(clan):
        if clan == Kuirk.name:
            return ConcreteKuirkFactory()
        elif clan == Strolth.name:
            return ConcreteStrolthFactory()
        elif clan == Ranger.name:
            return ConcreteRangerFactory()
        else:
            raise Exception("{} is not a known clan type".format(clan))
