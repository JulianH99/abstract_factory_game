from abc import ABC, abstractmethod
from ..factories.sprite_factories import PlayerFactory
from ..factories.abstract_clan_factory import FactoryClanAbsFact


class SpriteBuilder(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def build_body(self, gender: str):
        pass

    @abstractmethod
    def build_accessories(self, clan: str):
        pass

    @abstractmethod
    def get_object(self):
        pass


class PlayerBuilder(SpriteBuilder):

    def __init__(self):
        super(SpriteBuilder, self).__init__()
        self._body = None
        self._accessories = None

    def build_body(self, gender: str):
        self._body = PlayerFactory.factory_method(gender)

    def build_accessories(self, clan: str):
        self._accessories = FactoryClanAbsFact.factory_method(clan).get_clan_sprite()

    def get_object(self):
        return self._body, self._accessories



