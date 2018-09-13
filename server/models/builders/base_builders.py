from abc import ABC, abstractmethod
from ..factories.sprite_factories import PlayerFactory
from ..factories.abstract_clan_factory import FactoryClanAbsFact
from ..base import Player


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
        self._gender = None

    def build_body(self, gender: str):
        self._gender = gender
        self._body = PlayerFactory.factory_method(gender)
        self._body.complete_sprite = Player.get_body_from_gender(gender)

    def build_accessories(self, clan: str):
        if self._gender is None:
            raise Exception("Cant generate clothes before the body")
        self._accessories = FactoryClanAbsFact.factory_method(clan).get_clan_sprite()
        self._accessories.sprite_clothes = self._accessories.get_clothes(self._gender)

    def get_object(self):
        return self._body, self._accessories



