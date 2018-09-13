from abc import ABCMeta
from .base import Sprite
from typing import List, Dict
from .ships import Ship


class Clan(Sprite, metaclass=ABCMeta):
    _ships: List[Ship]
    _specialized_attributes: Dict[str, Dict[str, int]]
    name: str

    def __init__(self, specialized_attributes: Dict[str, Dict[str, int]]):
        super(Sprite, self).__init__()
        self._specialized_attributes = specialized_attributes
        self._ships = None
        self._sprite_clothes = ''

    @property
    def ships(self) -> List[Ship]:
        return self._ships

    @ships.setter
    def ships(self, new_ships: List[Ship]):
        self._ships = new_ships

    @property
    def specialized_attributes(self) -> Dict[str, Dict[str, int]]:
        return self._specialized_attributes

    @specialized_attributes.setter
    def specialized_attributes(self, new_specialized_attributes: Dict[str, Dict[str, int]]):
        self._specialized_attributes = new_specialized_attributes

    @property
    def sprite_clothes(self):
        return self._sprite_clothes

    @sprite_clothes.setter
    def sprite_clothes(self, new_value: str):
        self._sprite_clothes = new_value

    def get_json(self) -> Dict:
        json_dict = super().get_json()

        json_dict['name'] = self.name
        json_dict['clothes'] = self.sprite_clothes

        return json_dict

    def get_clothes(self, gender):
        if gender == 'male':
            return "ClothesMen{0}".format(self.name.capitalize())


class Kuirk(Clan):
    """
    Specialized in driving the AgileShip
    """

    name = "kuirk"
    
    def __init__(self):
        super(Clan, self).__init__()
        # set sprite name
        self._sprite_name = "SymbolKuirk"
        self._sprite_clothes = ''


        # set clan specialized attributes for ship
        specialized_attributes = {
            "heavy": {
                "speed": 50,
                "resistance": 70,
                "attack": 65
            },
            "agile": {
                "speed": 80,
                "resistance": 60,
                "attack": 80
            },
            "smart": {
                "speed": 70,
                "resistance": 60,
                "attack": 70
            },
        }

        self._specialized_attributes = specialized_attributes


class Ranger(Clan):
    """
    Specialized in driving the SmartShip
    """
    name = "ranger"

    def __init__(self):
        super(Clan, self).__init__()

        self._sprite_name = "SymbolRanger"
        self._sprite_clothes = ''

        specialized_attributes = {
            "heavy": {
                "speed": 50,
                "resistance": 70,
                "attack": 70
            },
            "agile": {
                "speed": 70,
                "resistance": 50,
                "attack": 70
            },
            "smart": {
                "speed": 80,
                "resistance": 70,
                "attack": 90
            },
        }

        self._specialized_attributes = specialized_attributes


class Strolth(Clan):
    """
    Specialized in driving the HeavyShip
    """
    
    name = "strolth"

    def __init__(self):
        super(Clan, self).__init__()

        self._sprite_name = "SymbolStrolth"
        self._sprite_clothes = ''

        specialized_attributes = {
            "heavy": {
                "speed": 60,
                "resistance": 80,
                "attack": 75
            },
            "agile": {
                "speed": 60,
                "resistance": 50,
                "attack": 65
            },
            "smart": {
                "speed": 60,
                "resistance": 60,
                "attack": 70
            },
        }

        self._specialized_attributes = specialized_attributes

